#!/usr/bin/env python3
"""Evaluate NuFIT-style DeltaChi2 grids at a given parameter point.

This script is designed to make the DFD neutrino appendix verifiable against
*published* global-fit likelihoods (NuFIT, etc.) without handwaving.

Expected input formats (common in global-fit data dumps):

1) 1D profile: two columns
   x  dchi2

2) 2D grid (rectangular): three columns
   x  y  dchi2

The script will:
- parse the file
- detect 1D vs 2D
- interpolate dchi2 at the requested point

Usage examples:
  python scripts_nufit_chi2_eval.py --file v60_dm21_dm3l_NO.dat --x 7.42e-5 --y 2.51e-3
  python scripts_nufit_chi2_eval.py --file v60_dm21_NO_1d.dat --x 7.42e-5

Notes:
- For 2D it uses linear interpolation on a Delaunay triangulation.
- If your grid is huge, consider converting to a regular mesh and using
  RectBivariateSpline.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

import numpy as np

try:
    from scipy.spatial import Delaunay
except ImportError:
    Delaunay = None


@dataclass
class Result:
    dchi2: float
    method: str
    in_hull: bool


def load_cols(path: str) -> np.ndarray:
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            parts = s.split()
            # allow comma-separated too
            if len(parts) == 1 and "," in parts[0]:
                parts = parts[0].split(",")
            try:
                vals = [float(p) for p in parts]
            except ValueError:
                continue
            data.append(vals)
    if not data:
        raise ValueError(f"No numeric data found in {path}")
    arr = np.asarray(data, dtype=float)
    return arr


def interp_1d(arr: np.ndarray, x: float) -> Result:
    if arr.shape[1] < 2:
        raise ValueError("1D profile needs at least 2 columns: x dchi2")
    xs = arr[:, 0]
    ys = arr[:, 1]
    # sort by x
    idx = np.argsort(xs)
    xs = xs[idx]
    ys = ys[idx]
    if x < xs[0] or x > xs[-1]:
        return Result(float("nan"), "1D-linear(outside-range)", False)
    d = float(np.interp(x, xs, ys))
    return Result(d, "1D-linear", True)


def interp_2d(arr: np.ndarray, x: float, y: float) -> Result:
    if arr.shape[1] < 3:
        raise ValueError("2D grid needs at least 3 columns: x y dchi2")
    if Delaunay is None:
        raise RuntimeError("scipy is required for 2D interpolation (pip install scipy)")

    pts = arr[:, 0:2]
    vals = arr[:, 2]

    tri = Delaunay(pts)
    p = np.array([[x, y]], dtype=float)
    simplex = tri.find_simplex(p)
    in_hull = bool(simplex >= 0)
    if not in_hull:
        return Result(float("nan"), "2D-delaunay(outside-hull)", False)

    # barycentric interpolation on the simplex
    s = int(simplex[0])
    X = tri.transform[s, :2]
    r = p[0] - tri.transform[s, 2]
    b = np.dot(X, r)
    bary = np.concatenate((b, [1 - b.sum()]))

    verts = tri.simplices[s]
    d = float(np.dot(bary, vals[verts]))
    return Result(d, "2D-delaunay-barycentric", True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True)
    ap.add_argument("--x", type=float, required=True)
    ap.add_argument("--y", type=float, default=None)
    args = ap.parse_args()

    arr = load_cols(args.file)

    if args.y is None:
        res = interp_1d(arr, args.x)
        print(f"dchi2(x={args.x:g}) = {res.dchi2}  [{res.method}]\n")
    else:
        # Determine if file is 2D or multiple columns.
        # If more than 3 columns, ignore extras.
        res = interp_2d(arr[:, :3], args.x, args.y)
        print(f"dchi2(x={args.x:g}, y={args.y:g}) = {res.dchi2}  [{res.method}]\n")

    if math.isfinite(res.dchi2):
        print(f"sigma_equiv ~ sqrt(dchi2) = {math.sqrt(res.dchi2):.3f} (for 1 dof heuristic)\n")
    else:
        print("Point is outside the provided grid/profile range.\n")


if __name__ == "__main__":
    main()
