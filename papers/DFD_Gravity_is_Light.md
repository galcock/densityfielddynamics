---
source_pdf: DFD_Gravity_is_Light.pdf
site: https://densityfielddynamics.com/
author: Gary Alcock
framework: Density Field Dynamics (DFD)
format_note: "Markdown extracted from the source PDF for clean AI ingestion. No editorial changes; mathematical typography in the PDF is authoritative."
---

Gravity is Light
A New Picture of the Universe

Gravity is Light
A New Picture of the Universe
A Complete Layperson’s Guide to
Density Field Dynamics

light bends

ψ field

mass

Gary Alcock

February 2026

Technical reference: DFD Unified Review v3.1
DOI: 10.5281/zenodo.18066593

2

© 2026 Gary Alcock. All rights reserved.
This book is a layperson’s companion to the technical paper:
Density Field Dynamics: A Unified Review (v3.1)
DOI: 10.5281/zenodo.18066593
Typeset in Charter and Helvetica.
Figures created with TikZ and PGFPLOTS.
Core promise to the reader:
“We are going to show you a completely different picture of gravity —
one where space doesn’t curve, but light slows down.
We’ll show you how that single idea resolves five of the biggest mysteries in physics.
And we’ll tell you exactly how you could prove us wrong.”

Contents
Preface: A Note on Honesty

11

I

13

The Problem

1 Einstein Was Right — And That’s the Problem
1.1 A Century of Being Right . . . . . . . . . . . . . . . . . . . .

15

1.2 The Dark Sector Problem . . . . . . . . . . . . . . . . . . . .

16

1.3 The Acceleration Coincidence . . . . . . . . . . . . . . . . .

17

1.4 What a Better Theory Would Look Like . . . . . . . . . . . .

18

2 The Road Not Taken — Gravity as Optics

II

15

22

2.1 Light Doesn’t Always Travel in Straight Lines . . . . . . . . .

22

2.2 Fermat’s Principle: Light Takes the Fastest Route . . . . . . .

23

2.3 The Optical Gravity Idea . . . . . . . . . . . . . . . . . . . .

24

2.4 Fermat Meets Newton . . . . . . . . . . . . . . . . . . . . .

24

The Theory

27

3 The Field — What ψ Is and Why It Works

29

3.1 The Refractive Index of Space . . . . . . . . . . . . . . . . .

29

3.2 The Field Equation . . . . . . . . . . . . . . . . . . . . . . .

30

3.3 The Throttle Function — Where Galaxies Come From . . . .

31

3.4 No Free Parameters . . . . . . . . . . . . . . . . . . . . . . .

33

5

CONTENTS

4 Passing Einstein’s Tests

35

4.1 The PPN Framework — How We Compare Gravity Theories

35

4.2 The Classic Tests . . . . . . . . . . . . . . . . . . . . . . . .

35

4.3 Gravitational Waves . . . . . . . . . . . . . . . . . . . . . .

35

4.4 Black Holes and the Event Horizon Telescope . . . . . . . .

37

5 Galaxies Without Dark Matter

III

38

5.1 Vera Rubin’s Puzzle . . . . . . . . . . . . . . . . . . . . . . .

38

5.2 Why Dark Matter Halos Are Uncomfortable . . . . . . . . .

38

5.3 DFD’s Answer: The Crossover . . . . . . . . . . . . . . . . .

39

5.4 The Baryonic Tully-Fisher Relation . . . . . . . . . . . . . .

39

5.5 The SPARC Test . . . . . . . . . . . . . . . . . . . . . . . . .

41

5.6 Galaxy Clusters . . . . . . . . . . . . . . . . . . . . . . . . .

41

The Numbers

43

6 Gravity Lives on a 7-Dimensional Shape
6.1 What is Topology? . . . . . . . . . . . . . . . . . . . . . . .
2

3

45
45

6.2 The Shape DFD Lives On: CP × S . . . . . . . . . . . . . .

46

6.3 Where the Throttle Function Comes From . . . . . . . . . .

46

6.4 Where the Crossover Acceleration Comes From . . . . . . .

47

7 The Most Mysterious Number in Physics — And Where It Comes
From

48

7.1 The Fine Structure Constant . . . . . . . . . . . . . . . . . .

48

7.2 The Chern-Simons Calculation . . . . . . . . . . . . . . . . .

49

7.3 Why This Is Not Numerology . . . . . . . . . . . . . . . . .

50

7.4 What Else Follows from the Topology . . . . . . . . . . . . .

51

6

CONTENTS

8 Nine Masses From One Formula

IV

53

8.1 The Particle Mass Puzzle . . . . . . . . . . . . . . . . . . . .

53

8.2 The DFD Formula . . . . . . . . . . . . . . . . . . . . . . . .

53

8.3 The Results . . . . . . . . . . . . . . . . . . . . . . . . . . .

54

The Cosmos

56

9 The Universe Isn’t Accelerating — It Just Looks That Way
9.1 The 1998 Surprise . . . . . . . . . . . . . . . . . . . . . . .

57

9.2 What “Faint” Actually Means . . . . . . . . . . . . . . . . . .

58

9.3 The ψ-Screen . . . . . . . . . . . . . . . . . . . . . . . . . .

58

9.4 Three Independent Measurements That Must Agree . . . . .

59

9.5 The Hubble Tension — Resolved

59

. . . . . . . . . . . . . . .

10 The CMB — Sound Frozen in Light

V

57

61

10.1 The Oldest Light in the Universe . . . . . . . . . . . . . . . .

61

10.2 The Acoustic Peaks . . . . . . . . . . . . . . . . . . . . . . .

61

10.3 DFD’s CMB . . . . . . . . . . . . . . . . . . . . . . . . . . .

61

The Verdict

63

11 Atomic Clocks — The Most Important Experiment You’ve Never
Heard Of

65

11.1 The World’s Most Precise Instruments . . . . . . . . . . . . .

65

11.2 What GR Predicts for Clocks . . . . . . . . . . . . . . . . . .

65

11.3 What DFD Predicts — And Why It’s Different . . . . . . . . .

66

11.4 The Cavity Test — Even Cleaner . . . . . . . . . . . . . . . .

67

7

CONTENTS

12 One Test Already Confirmed — The Solar Corona
12.1 The Solar Wind Problem . . . . . . . . . . . . . . . . . . . .

68

12.2 The DFD Prediction . . . . . . . . . . . . . . . . . . . . . . .

68

12.3 The Measurement . . . . . . . . . . . . . . . . . . . . . . . .

68

13 How to Break DFD — The Falsification Map

VI

68

71

13.1 Why Falsifiability Matters . . . . . . . . . . . . . . . . . . .

71

13.2 The Five Binary Discriminators . . . . . . . . . . . . . . . .

71

13.3 Direct Dark Matter Detection . . . . . . . . . . . . . . . . .

71

13.4 An Invitation . . . . . . . . . . . . . . . . . . . . . . . . . .

72

The Deeper Picture

74

14 A Universe Without Dark Inventory

75

14.1 The End of the Dark Sector . . . . . . . . . . . . . . . . . .

75

14.2 The Standard Model from Geometry . . . . . . . . . . . . .

75

14.3 Strong CP Without the Axion . . . . . . . . . . . . . . . . .

76

14.4 What Remains Unknown . . . . . . . . . . . . . . . . . . . .

76

15 What Is the Medium?

78

15.1 The Old Ether Problem . . . . . . . . . . . . . . . . . . . . .

78

15.2 The Difference . . . . . . . . . . . . . . . . . . . . . . . . .

78

15.3 The Open Question . . . . . . . . . . . . . . . . . . . . . . .

79

A The Equations — A Glossary

80

B The Evidence — A Summary Table

81

C The Falsification Map

83

D For the Skeptical Physicist

84
8

CONTENTS

E Further Reading

86

9

Preface: A Note on Honesty
“The first principle is that you must not fool yourself — and
you are the easiest person to fool.”
— Richard P. Feynman

I am not a professor. I do not have a PhD in physics. I work in finance during
the day, and I work on physics in every other hour I can find. I tell you this
upfront because honesty is the only currency that matters in science.
The theory in this book — Density Field Dynamics — began with a simple
question: what if gravity isn’t curved spacetime, but a refractive medium?
What if light doesn’t bend near the Sun because space is warped, but because
light slows down in the region near a mass, exactly the way it slows down in
glass or water?
That question led, over years of work, to a complete mathematical
framework. One that reproduces every test of Einstein’s General Relativity.
One that explains why galaxies spin flat without invoking invisible matter.
One that derives the fine structure constant — the most mysterious number
in physics — from pure geometry. One that makes specific, quantitative
predictions that can be tested with instruments that already exist.
I want to be clear about what this book is and isn’t.
What it is: An honest guide to a new theory. Every claim is backed by a
specific equation, a specific dataset, or a specific experimental prediction.
When something is derived, I’ll say “derived.” When something is assumed,
I’ll say “assumed.” When something is incomplete or uncertain, I’ll say that
too.
What it isn’t: An appeal to authority. I have none. What I have instead is
11

Preface

a theory that makes falsifiable predictions — predictions that can be tested
and that would kill the theory if they come out wrong.
That’s the deal I’m making with you. I’ve told you exactly how to break
this theory. Now I invite you to try.

The reader’s compact: I’ll be honest about what’s proven,
what’s derived, and what’s still a guess. In return, I ask only
that you follow the logic.

— Gary Alcock, February 2026
12

Part I
The Problem

Why physics needed a new idea

13

Chapter 1
Einstein Was Right — And That’s the
Problem
“The most incomprehensible thing about the universe is that it
is comprehensible.”
— Albert Einstein

1.1

A Century of Being Right

In 1915, Albert Einstein published a set of equations that redefined our
understanding of gravity. His theory — General Relativity — said something
astonishing: massive objects don’t pull on each other through empty space.
Instead, they warp the fabric of spacetime itself. Everything — planets, light,
even time — follows the contours of that warping.
It was a bold claim, and nature confirmed it. In 1919, Arthur Eddington
measured starlight bending around the Sun during a solar eclipse, exactly
as Einstein predicted. Mercury’s orbit, which had stubbornly refused to
match Newton’s equations for decades, finally agreed with the new theory
to exquisite precision: 42.98 arcseconds of precession per century. Radio
signals passing near the Sun slow down by exactly the predicted amount
— the Shapiro delay. And in 2015, a century after Einstein published
his equations, the LIGO detectors heard the spacetime vibrations from
15

CHAPTER 1. EINSTEIN WAS RIGHT — AND THAT’S THE PROBLEM

two colliding black holes — gravitational waves, ringing at precisely the
frequency General Relativity predicted.

General Relativity has never once been wrong in any experiment we’ve done in the solar system.
So why propose something different? Because Einstein’s triumph comes
at a breathtaking price.

1.2

The Dark Sector Problem

In 1933, the Swiss astronomer Fritz Zwicky was studying the Coma galaxy
cluster — a swarm of over a thousand galaxies bound together by gravity. He
measured how fast the individual galaxies were moving, and he calculated
how much mass the cluster needed to hold itself together. The answer was
alarming: the cluster needed roughly ten times more mass than its visible
stars could provide. Zwicky called the missing ingredient dunkle Materie —
dark matter.
For decades, his observation was treated as a curiosity. Then, in the
1970s, the astronomer Vera Rubin changed everything. Rubin and her
colleague Kent Ford measured the rotation speeds of stars in spiral galaxies.
According to Newton and Einstein, stars in the outer reaches of a galaxy
should orbit slowly — just as Neptune orbits the Sun more slowly than
Mercury. The gravitational pull of the visible matter should weaken with
distance.
That’s not what Rubin found. The outer stars were moving just as fast
as the inner ones. The rotation curves were flat, not falling. Something
invisible was holding the galaxies together.
16

1.3. THE ACCELERATION COINCIDENCE

The problem only deepened. In 1998, two teams of astronomers — led
by Saul Perlmutter and Adam Riess — discovered that distant supernovae
were fainter than expected. The universe wasn’t just expanding; it was
accelerating. Whatever was pushing it apart was dubbed “dark energy.”
The cosmic accounting now looks like this: ordinary matter — the atoms
that make up you, me, the Earth, every star in every galaxy — accounts
for roughly 5% of the total energy content of the universe. Dark matter
accounts for 27%. Dark energy accounts for 68%.

In any other field of science, if your model required 95% of
its ingredients to be undetected, you’d suspect the model.

1.3

The Acceleration Coincidence

There is a strange number hiding in the galaxy rotation data. Below a characteristic gravitational acceleration of about a0 ≈ 1.2 × 10−10 m/s2 , galaxies
consistently depart from Newtonian predictions. Above that threshold,
everything looks normal.
In 1983, the Israeli physicist Mordehai Milgrom noticed something remarkable. This number a0 is eerily close to the product of the speed of light
and the Hubble constant: c × H0 . The scale at which individual galaxies go
strange is connected to the scale of the entire observable universe.
17

CHAPTER 1. EINSTEIN WAS RIGHT — AND THAT’S THE PROBLEM

The Acceleration Coincidence
Standard Cosmology (ΛCDM)
Density Field Dynamics

“It’s a coincidence. Dark matter

1.4

halos just happen to produce

“It’s a derivation. The crossover
√
acceleration is a∗ = 2 α c H0 ,

dynamics that mimic this

derived from the topology of the

threshold.”

microsector.”

What a Better Theory Would Look Like

Before we build the alternative, let’s agree on the standards it must meet. A
viable replacement for standard gravity would need to:

1. Reproduce every GR success — Mercury’s perihelion, light bending,
Shapiro delay, gravitational waves — to the same precision.

2. Explain galaxy dynamics without invoking an invisible substance that
has never been directly detected.

3. Explain cosmic acceleration without invoking an invisible energy that
violates quantum mechanical expectations by 120 orders of magnitude.

4. Make new, falsifiable predictions — specific tests that could prove it
wrong.

Such a theory exists. Let’s build it.
18

1.4. WHAT A BETTER THEORY WOULD LOOK LIKE

Chapter Summary
The DFD one-liner: Einstein’s gravity works perfectly — but it needs
95% of the universe to be invisible. DFD asks: what if the model, not
the universe, needs fixing?
What would confirm this chapter’s premise: Continued nondetection of dark matter particles. Growing tension in cosmological
parameters. New anomalies at the a0 threshold.
What would break it: Direct laboratory detection of a dark matter particle with properties consistent across multiple experiments.
Resolution of all galactic anomalies within ΛCDM without fine-tuning.

19

CHAPTER 1. EINSTEIN WAS RIGHT — AND THAT’S THE PROBLEM

Rotation speed (km/s)

250
200
The gap
Observed (flat!)
(“dark matter”)
Predicted (visible matter only)

150
100
50
0
0

5

10

15

20

25

30

35

Distance from galaxy center (kpc)

Figure 1.1: The galaxy rotation curve puzzle. Stars in the outskirts of
galaxies orbit just as fast as stars near the center. The blue dashed line
shows what visible matter alone predicts. The orange line is what we
actually observe. The gap between them is what physics calls “dark matter.”
Or is it?

20

1.4. WHAT A BETTER THEORY WOULD LOOK LIKE

Everything you’ve ever seen

You
5%

Dark
27% Matter
68%
Dark Energy
Never detected

Figure 1.2: The cosmic budget. We’ve detected 5%. The other 95% is a
placeholder for our ignorance.

21

Chapter 2
The Road Not Taken — Gravity as Optics
“Nature uses only the longest threads to weave her patterns,
so each small piece of her fabric reveals the organization of
the entire tapestry.”
— Richard P. Feynman

2.1

Light Doesn’t Always Travel in Straight Lines

Put a straw in a glass of water. It appears to bend at the surface. Drive down
a highway on a hot day. You see shimmering pools of “water” on the road
that vanish as you approach — a mirage. Watch a sunset. The Sun appears
above the horizon for several minutes after it has geometrically dropped
below it.
These are all the same phenomenon: light bending when it moves
through a medium where its speed changes. The rule governing this bending
was discovered by Willebrord Snell in 1621: light crossing a boundary
between materials bends toward the material where it travels slower.
The key concept is the refractive index, denoted n. It tells you how much
slower light travels in a medium compared to vacuum. In glass, n ≈ 1.5,
so light travels at about two-thirds its vacuum speed. In air, n ≈ 1.0003 —
22

2.2. FERMAT’S PRINCIPLE: LIGHT TAKES THE FASTEST ROUTE

barely different from vacuum, but enough to produce mirages and lingering

Refractive index n increases

sunsets.
eye

Cool (slow light)

actual light path

Hot (fast light)

“water” on road

Figure 2.1: The mirage effect. Hot air near the road surface has a lower
refractive index (light travels faster). Light from the sky curves upward,
creating the illusion of water on the road. This is exactly the physics DFD
uses for gravity — but with mass instead of heat creating the gradient.
The crucial insight: you don’t need a sharp boundary. If the refractive index changes gradually across space, light traces smooth curves. No surfaces,
no edges — just a continuous medium with varying properties.

2.2 Fermat’s Principle: Light Takes the Fastest Route
There’s a beautiful deep principle at work here. Light doesn’t “know” about
Snell’s Law. It simply takes the path that minimizes travel time — Fermat’s
Principle, discovered in 1662.
Think of it this way: if you’re a lifeguard who needs to reach a drowning
swimmer, and you run faster on sand than you swim in water, you wouldn’t
run straight toward them. You’d angle your path — running farther along
the beach and entering the water closer to the swimmer. The fastest path
isn’t the straightest one.
23

CHAPTER 2. THE ROAD NOT TAKEN — GRAVITY AS OPTICS

Light does the same thing. And if you fill all of space with a varying
refractive index, light will trace curved paths through that space — even
though the space itself is perfectly flat.

2.3

The Optical Gravity Idea

Here’s a historical fact that most physics students are never taught. In
1911 — four years before completing General Relativity — Einstein himself
calculated that light should bend near the Sun. He did this calculation
using a varying speed of light near a massive body, treating gravity as a
kind of optical effect. He got half the right answer. The other half, he later
concluded, came from the curvature of space itself.
DFD asks a provocative question: what if both halves are optical?
What if there is no curved spacetime — only a scalar field ψ (pronounced
“sigh”) that permeates all of space and acts like a refractive index? Where
ψ is stronger, light slows down, clocks run slower, and objects accelerate —
exactly as they would in an optical medium.

DFD’s founding idea: replace the curved fabric of spacetime
with a refractive medium. Every prediction of General Relativity follows.

2.4

Fermat Meets Newton

In an optical medium, objects moving slowly compared to light still feel the
gradient of the refractive index. The acceleration of a massive body is:
24

2.4. FERMAT MEETS NEWTON

a=

c2
∇ψ
2

(2.1)

In plain English: Things accelerate toward regions where ψ is larger
— where light is slower. The factor c2 /2 sets the scale. This is Newton’s
gravity, rewritten as optics.

Einstein’s Picture

DFD’s Picture

ψ field

“Space is curved.
Objects follow the curvature.”

“Space is flat.
The medium is
denser near mass.”

Figure 2.2: Two pictures of gravity. Left: Einstein’s curved spacetime — a
rubber sheet deformed by mass. Right: DFD’s refractive medium — a flat
space with a varying ψ field. Both predict the same observations in the solar
system. They diverge in galaxies and cosmology.

The optical metric in DFD is simple and explicit:
ds̃2 = −

c2 dt2
+ dx2
n2
25

(2.2)

CHAPTER 2. THE ROAD NOT TAKEN — GRAVITY AS OPTICS

In plain English: Space is flat (dx2 is just ordinary Euclidean distance).
Time runs at a rate set by the refractive index n = eψ . Where ψ is
large, n is large, and clocks tick slower. That’s it.
Two Languages for Gravity
Einstein says:

DFD says:

“Space is curved.”

“The medium is denser.”

“Objects follow geodesics.”

“Objects follow refractive

“Time dilates because of

gradients.”

curvature.”

“Time dilates because n = eψ .”

How to tell them apart: Look at galaxies. Look at atomic clocks. Look at the cosmic
microwave background.

Chapter Summary
The DFD one-liner: Gravity is not curved spacetime. It’s light slowing
down in a refractive medium — and everything else follows.
What would confirm: DFD-specific predictions (clock anomalies,
galaxy dynamics without dark matter) matching observation.
What would break it: A genuine geometric effect of gravity that cannot be replicated optically — such as topology change in gravitational
collapse that has measurable external consequences.

26

Part II
The Theory

What DFD actually says, piece by piece

27

Chapter 3
The Field — What ψ Is and Why It Works
3.1

The Refractive Index of Space

The ψ field is the simplest kind of physical field: a scalar field. At every
point in space, ψ is just a single number — like temperature on a weather
map, or altitude on a topographic map. There’s no direction to it, no vector,
no tensor. Just a number.
The refractive index of space is:
n = eψ

(3.1)

In plain English: eψ is the exponential of ψ. When ψ = 0 (far from any
mass), n = 1 — vacuum. When ψ is positive (near a mass), n > 1 —
light slows down, clocks run slower, objects accelerate inward. That’s
gravity.
Near a spherical mass M , the ψ field takes a simple form: ψ ≈ GM/(rc2 ),
where r is the distance from the center. The gradient points inward. Objects
accelerate inward. That’s gravity — rewritten as optics.

29

CHAPTER 3. THE FIELD — WHAT ψ IS AND WHY IT WORKS

Strong ψ

ψ

∇

Earth ψ high

ψ low

ψ field

Weak ψ

Figure 3.1: The ψ field around Earth. Near the surface, ψ is strongest —
clocks run slowest, light bends most. Moving away, ψ weakens. The arrows
show ∇ψ, the gradient — the direction of gravitational acceleration.

3.2

The Field Equation

Every field theory needs an equation telling the field how to respond to
matter. DFD’s field equation is:

 


|∇ψ|
8πG
∇ψ = − 2 ρ
∇· µ
a∗
c
30

(3.2)

3.3. THE THROTTLE FUNCTION — WHERE GALAXIES COME FROM

Piece by piece:
• ∇ψ — the slope of ψ, how fast it changes across space. This is what
produces acceleration.
• µ(x) — a “throttle function.” When gravity is strong, µ ≈ 1 (full
strength). When gravity is very weak, µ ≈ x (reduced throttle).
This is where galaxies come from.
• ρ — the density of ordinary matter. Stars, gas, dust. The only
source.
• G and c — Newton’s gravitational constant and the speed of light.
The sentence version: Matter tells ψ how to arrange itself; ψ tells
matter how to move.

This one equation, with no free parameters, governs gravity
from the Solar System to the edge of the observable universe.

3.3 The Throttle Function — Where Galaxies Come
From
The function µ(x) is the key to everything:
µ(x) =

x
1+x

(3.3)

When gravity is strong — in the solar system, near black holes, anywhere
the acceleration exceeds a∗ — the throttle is wide open: µ ≈ 1. The field
equation reduces to exactly what GR predicts. Every solar system test passes
31

CHAPTER 3. THE FIELD — WHAT ψ IS AND WHY IT WORKS

Solar system: µ ≈ 1

µ≈x

y
ax

al

0.5

Crossover: a = a∗

ou
t

sk

ir t
s

0.75

G

µ(x)

(throttle)

1

0.25
0
0

1

2
4
x = |∇ψ|/a∗

6

8

10

(gravitational strength)

Figure 3.2: The throttle function µ(x) = x/(1 + x). When gravity is strong
(x ≫ 1), µ = 1 and DFD is identical to GR. When gravity is weak (x ≪ 1),
µ = x and the field equation changes character — rotation curves flatten.
The crossover happens at a∗ ≈ 1.2 × 10−10 m/s2 .

automatically.
When gravity is very weak — in the outskirts of galaxies, where the
acceleration drops below a∗ — the throttle closes: µ ≈ x. The equation
changes character. The effective gravitational force strengthens relative
to what Newton would predict. Rotation curves flatten. No dark matter
required.
The critical insight: this crossover function is not fitted to data. It is
derived from the geometry of a 7-dimensional mathematical space called
32

3.4. NO FREE PARAMETERS

CP2 × S 3 . We’ll meet this space in Chapter 6.
Where Does µ(x) Come From?
MOND (Milgrom, 1983)

DFD

Milgrom chose µ(x) to fit galaxy

µ(x) = x/(1 + x) is the unique

data. Multiple functional forms

output of a geometric theorem

work. It’s an empirical guess.

about the 3-sphere. It’s derived,
not chosen.

3.4

No Free Parameters

This claim sounds bold, and it is: DFD has zero continuous adjustable
parameters.
The full ledger: two foundational postulates (n = eψ and a = (c2 /2)∇ψ),
topological integers from the Standard Model structure, and one measured
scale (the Hubble constant H0 , or equivalently Newton’s constant G). Everything else — the fine structure constant, galaxy rotation curves, the
crossover acceleration, fermion masses — is derived.

You measure one number. Everything else follows.
33

CHAPTER 3. THE FIELD — WHAT ψ IS AND WHY IT WORKS

Chapter Summary
The DFD one-liner: A single scalar field ψ, obeying one nonlinear
equation with no free parameters, produces Newtonian gravity in
strong fields and flat rotation curves in weak fields.
What would confirm: Rotation curve fits across hundreds of galaxies
with zero adjustable parameters beyond known baryonic mass.
What would break it: A galaxy whose rotation curve systematically deviates from the DFD prediction by more than 3σ, with wellmeasured baryonic mass.

34

Chapter 4
Passing Einstein’s Tests
4.1 The PPN Framework — How We Compare Gravity
Theories
Physicists have a standardized language for comparing theories of gravity:
the Parameterized Post-Newtonian (PPN) framework. It defines ten parameters — with names like γ, β, ξ, α1 through α3 , and ζ1 through ζ4 — that
characterize how any gravity theory behaves in the weak-field, slow-motion
limit.
General Relativity’s values: γ = β = 1, all others zero. These have been
tested to extraordinary precision.
DFD’s values: identical. γ = β = 1. All ten parameters match GR exactly.

DFD passes every PPN test by construction — not by luck.

4.2

The Classic Tests

4.3

Gravitational Waves

On August 17, 2017, LIGO and Virgo detected gravitational waves from a
binary neutron star merger — event GW170817. Crucially, a gamma-ray
35

CHAPTER 4. PASSING EINSTEIN’S TESTS

Test

GR Predicts

DFD Predicts

Status

Mercury perihelion

42.98′′ /cy

42.98′′ /cy

Light deflection

1.75′′

1.75′′

Shapiro delay

∆tGR

∆tGR

✓
✓
✓
✓

Gravitational
red- ∆f /f = g h/c2
shift
GW speed (cT )
c

∆f /f = g h/c2
c

GW polarizations

2 tensor

2 tensor

Frame-dragging

ΩGR

ΩGR

✓
✓
✓

Figure 4.1: Every classical test of gravity: GR and DFD give identical
predictions. The green checkmarks mean the observation matches both
theories to within experimental precision.

burst was detected 1.7 seconds later, after both signals had traveled 130
million light-years.
This single observation tells us that gravitational waves travel at the
speed of light to better than one part in 1015 . This measurement killed
dozens of competing gravity theories that predicted cT ̸= c.
DFD predicts cT = c exactly. Two tensor polarizations, exactly as GR
predicts.

GW170817 killed dozens of competing theories. DFD survived.

36

4.4. BLACK HOLES AND THE EVENT HORIZON TELESCOPE

4.4

Black Holes and the Event Horizon Telescope

DFD predicts photon spheres — regions where light can orbit a compact
object — at the same locations GR predicts. The shadows of M87* and
Sgr A* observed by the Event Horizon Telescope are consistent with DFD.
The difference is interpretive: DFD calls them “optical horizons” rather
than singularities in spacetime. What’s different inside: DFD avoids the
information paradox by having no fundamental singularity.

Chapter Summary
The DFD one-liner: DFD isn’t fighting Einstein. It’s reinterpreting
him — and passes every test he passed.
What would confirm: New precision measurements continuing to
match both GR and DFD.
What would break it: Detection of a gravitational effect that is
genuinely geometric (not optical) — such as spacetime topology
change with externally measurable consequences.

37

Chapter 5
Galaxies Without Dark Matter
“The important thing in science is not so much to obtain new
facts as to discover new ways of thinking about them.”
— Sir William Bragg

5.1

Vera Rubin’s Puzzle

In the 1970s, Vera Rubin and Kent Ford at the Carnegie Institution measured
something that should have been routine: the rotation speeds of stars in
spiral galaxies. Plot the orbital velocity against distance from the center.
Textbook exercise.
Except the data refused to follow the textbook. Stars far from the galactic
center orbited just as fast as stars near the center. The rotation curves were
flat.
This has now been measured for thousands of galaxies. It’s always flat.

5.2

Why Dark Matter Halos Are Uncomfortable

The standard explanation: an enormous halo of invisible matter surrounds
every galaxy, providing extra gravitational pull that keeps the outer stars
moving fast. This could be true. But notice what we’re doing: for every
galaxy, we infer a dark matter halo by working backward from what the
38

5.3. DFD’S ANSWER: THE CROSSOVER

rotation curve needs. We’ve been doing this for fifty years. We’ve never
detected a dark matter particle directly.
Worse: the inferred halos have properties that seem to “know about” the
visible matter in ways that dark matter shouldn’t care about. The Radial
Acceleration Relation (RAR) shows a tight, universal correlation between
the observed gravitational acceleration and the acceleration predicted from
baryonic matter alone. If dark matter is an independent, separately distributed component, why does it always arrange itself to match the baryonic
prediction so precisely?

If dark matter is a separate substance, why does it always
arrange itself in exactly the way ordinary matter demands?

5.3

DFD’s Answer: The Crossover

In DFD, there’s no invisible matter. The ψ field itself behaves differently
at low accelerations. When the gravitational acceleration falls below a∗ ≈
1.2 × 10−10 m/s2 — which happens in the outskirts of every galaxy — the
throttle function µ(x) shifts regime. The effective force strengthens, not
because of invisible matter, but because of how ψ responds to the baryonic
source.

5.4

The Baryonic Tully-Fisher Relation

One of the tightest empirical laws in extragalactic astronomy:
4
Vflat
= G Mbar a0

39

(5.1)

CHAPTER 5. GALAXIES WITHOUT DARK MATTER

The ψ field around a spiral galaxy

Crossover regime
Newtonian regime

µ≈1
µ ≈ x — rotation curves flatten

Figure 5.1: Galaxy dynamics in DFD. Near the center (white), the ψ field is
in the Newtonian regime — everything matches Newton/GR. In the outskirts
(gold), the field enters the crossover regime where µ ≈ x. Rotation curves
flatten automatically. No dark matter halo required.

In plain English: The flat rotation speed of any galaxy, raised to the
fourth power, equals its baryonic mass times a universal constant. This
holds across five decades in galaxy mass — from tiny dwarfs to giant
spirals.
Dark matter models struggle to explain why this relation is so tight and
universal. DFD derives it: in the deep-field limit, the field equation reduces
exactly to V 4 = G M a∗ .

The Tully-Fisher relation is not a lucky fit in DFD. It’s a
theorem.

40

5.5. THE SPARC TEST

5.5

The SPARC Test

The SPARC catalog provides the gold-standard dataset: 175 galaxies with
measured rotation curves and detailed baryonic mass maps (stars plus gas,
measured independently).
DFD’s task: given only the baryonic mass distribution, predict the full
rotation curve. No dark matter. No free parameters beyond each galaxy’s
own measured mass.
Result: DFD fits the data with residuals below 5%. DFD outperforms
Standard MOND in the transition regime where the two theories actually
differ.
DDO 154

NGC 3198

60

150

200

50

40

v (km/s)

v (km/s)

v (km/s)

150
100

20

100
50

0 2403
NGC
0

5

0
10

15

20

0
0

2

4

r (kpc)

6

r (kpc)

8

10

0

10

20

30

r (kpc)

Figure 5.2: Three SPARC galaxies: DFD predictions (orange) vs. observations (gray dots). A massive spiral (NGC 2403), a tiny dwarf (DDO 154),
and a large disk (NGC 3198). All predicted from baryonic mass alone. No
dark matter. No free parameters.

5.6

Galaxy Clusters

Clusters — the largest gravitationally bound structures — are harder. The
mass discrepancy is larger and the geometry is messier. Standard cosmology
requires enormous dark matter halos, often ten times the visible mass.
DFD’s resolution: when you carefully account for warm-hot intergalactic
medium (WHIM), intracluster light (ICL), and the mathematics of averaging
41

CHAPTER 5. GALAXIES WITHOUT DARK MATTER

non-uniform density, the discrepancy resolves. Analysis of 16 clusters:
Observed/DFD = 0.98 ± 0.05. All within 10% of unity.

Not dark matter. Baryons we forgot to count, and math we
did wrong.

Chapter Summary
The DFD one-liner: Galaxies don’t need dark matter. They need
a field equation that changes character at low accelerations — and
DFD’s equation does exactly that, from first principles.
What would confirm: Continued success across new galaxy samples, especially ultra-diffuse galaxies and tidal dwarf galaxies (which
standard models predict should have little dark matter).
What would break it: Systematic deviations > 3σ across multiple
independent galaxy samples.

42

Part III
The Numbers

Where DFD does something no other theory has done

43

Chapter 6
Gravity Lives on a 7-Dimensional Shape
6.1

What is Topology?

Topology is the study of shapes that don’t change when you stretch or
squeeze them — only when you cut or glue. A coffee mug and a donut are
topologically identical (each has exactly one hole). A sphere has no holes.
You can stretch a sphere all day long, but you’ll never turn it into a donut
without tearing it.

=
Donut

̸=
Coffee
mug
(1 hole)

(1 hole)

Sphere
(0 holes)

Figure 6.1: Topology in a nutshell. A donut and a coffee mug are topologically the same (one hole each). A sphere is fundamentally different (no
holes). Topological numbers are integers — they can’t be fine-tuned.
What makes topological numbers powerful: they’re integers. You can’t
have 1.3 holes. This means topological predictions can’t be adjusted or
fine-tuned. They’re either right or wrong.

45

CHAPTER 6. GRAVITY LIVES ON A 7-DIMENSIONAL SHAPE

6.2

The Shape DFD Lives On: CP2 × S 3

DFD posits that the fundamental structure of physics is encoded on a 7dimensional mathematical space: CP2 × S 3 .
CP2 (Complex Projective 2-space) is a 4-dimensional space with very
specific symmetry properties. S 3 (the 3-sphere) is the 3-dimensional surface
of a 4-dimensional ball — the space that wraps back on itself in every
direction.
Think of it this way: the surface of the Earth is a 2-sphere. As you walk
around on it day to day, you don’t notice the curvature. But it governs the
large-scale geometry — you can circumnavigate the globe and return to
your starting point. CP2 × S 3 is the “surface” on which the laws of physics
live.

6.3

Where the Throttle Function Comes From

On S 3 , there’s a natural composition law — a mathematical rule for combining two directions into a third (related to quaternion multiplication).
When you work out what this composition law implies for how ψ sources
and responds to matter at low accelerations, you get one specific function:

µ(x) =

x
1+x

This is a theorem — Theorem 12 in the technical paper. It is derived, not
chosen.
46

6.4. WHERE THE CROSSOVER ACCELERATION COMES FROM

The specific shape of the crossover function that fits all galaxy
rotation curves was not fitted to data. It is the unique output
of a geometric theorem about the 3-sphere.

6.4

Where the Crossover Acceleration Comes From

The crossover happens at:
√
a∗ = 2 α c H0
This links the scale at which individual galaxies go strange to the scale
of the entire observable universe. It also means that as the universe expands and H0 slowly changes, a∗ slowly changes — a prediction for future
astronomy.

Chapter Summary
The DFD one-liner: The laws of physics live on a 7-dimensional
shape, and the specific topology of that shape determines everything
from the crossover function to the fine structure constant.
What would confirm: Successful derivation of additional Standard
Model properties from the same topology.
What would break it: Discovery of a fourth generation of fermions
(the topology predicts exactly three).

47

Chapter 7
The Most Mysterious Number in Physics
— And Where It Comes From
“There is a most profound and beautiful question associated
with the observed coupling constant. . . It is a simple
number. . . one of the greatest damn mysteries of physics: a
magic number that comes to us with no understanding by
man.”
— Richard P. Feynman

7.1

The Fine Structure Constant

The fine structure constant, α, governs the strength of electromagnetism —
how strongly electrons interact with light. Its value:
α−1 ≈ 137.036
It is dimensionless: no units, no system of measurement can change it.
It is the same number everywhere in the universe.
If α were slightly different — say 1/100 or 1/200 — atoms as we know
them would not exist. Stars would not burn. Chemistry would not work.
Life would be impossible.
48

7.2. THE CHERN-SIMONS CALCULATION

Nobody has ever derived this number from first principles. Every other
theory in physics takes it as an input — measured, recorded, put in by hand.
For nearly a century, understanding why α ≈ 1/137 has been one of the
deepest open problems in fundamental physics.

If α were slightly different, atoms wouldn’t exist. For a
century, nobody could explain why it has the value it does.

7.2

The Chern-Simons Calculation

On CP2 × S 3 , there’s a mathematical object called the Chern-Simons form.
It counts how “twisted” the geometry is. When you compute the spectral
action — a sum over all the ways the geometry vibrates — and demand that
the answer comes in discrete, quantized units, you get a restriction on the
allowed coupling constants.
With the truncation level kmax = 60 (uniquely fixed by the Standard
Model’s gauge structure and a mathematical condition called “minimal
padding”), the quantization condition gives:
α−1 = 137.036

(7.1)

Agreement with the measured value: better than 0.001%.
This calculation has been verified by lattice Monte Carlo simulation: 86
independent runs on different lattice sizes, all converging on the same value.

49

CHAPTER 7. THE MOST MYSTERIOUS NUMBER IN PHYSICS — AND WHERE IT
COMES FROM
137.3

α−1

137.2
137.1
137.036
137.0

Measured
DFD
mean

136.9
136.8

0

10

20

30

40

50

60

70

80

90

Monte Carlo run number

Figure 7.1: Monte Carlo verification of the α derivation. 86 independent
lattice runs, each computing α−1 from the Chern-Simons quantization on
CP2 ×S 3 . All converge on the measured value of 137.036 to within statistical
error.

7.3

Why This Is Not Numerology

The honest concern: physics history is littered with people claiming to derive
137 from something clever. Eddington tried. Many others have tried. Most
turn out to be coincidences.
What’s different here: kmax = 60 is not chosen to fit α. It is forced by a
mathematical condition (minimal padding) combined with the Standard
Model’s known gauge structure. The calculation has no adjustable parameters. The verification uses lattice Monte Carlo — the same computational
technique used in precision QCD calculations — and independently confirms
the result.
50

7.4. WHAT ELSE FOLLOWS FROM THE TOPOLOGY

We derive kmax = 60 from Standard Model symmetry. Then
we run the Chern-Simons calculation. Then we read off α.
We never touch α to get α.

7.4

What Else Follows from the Topology

Once α is derived, a cascade of results follows. The Higgs vacuum expectation value — the energy scale responsible for giving all particles their
mass:

v = MP × α 8 ×

√

2π = 246.09 GeV

The observed value: 246.22 GeV. Agreement: 0.05%.
The hierarchy problem — why the Higgs scale is 17 orders of magnitude
below the Planck scale — is solved by eight powers of α. No fine-tuning. No
supersymmetry. Just topology.

The hierarchy problem — why the Higgs mass is so much
lighter than the Planck mass — is solved by eight powers of
the fine structure constant.
51

CHAPTER 7. THE MOST MYSTERIOUS NUMBER IN PHYSICS — AND WHERE IT
COMES FROM

Chapter Summary
The DFD one-liner: The most mysterious number in physics — α =
1/137 — is derived from the topology of CP2 × S 3 , with independent
Monte Carlo verification.
What would confirm: Independent groups reproducing the lattice
calculation with the same result.
What would break it: A different topology producing a comparably
accurate derivation of α with fewer assumptions. Or a measurement
of α at high energy that deviates from the predicted running.

52

Chapter 8
Nine Masses From One Formula
8.1

The Particle Mass Puzzle

The Standard Model has twelve fundamental fermions: six quarks and six
leptons. Their masses span thirteen orders of magnitude — the top quark
is roughly 350,000 times heavier than the electron. The Standard Model
offers no explanation for this hierarchy. Each mass is simply an input.

8.2

The DFD Formula

DFD proposes:

v
mf = Af × αnf × √
2

√
In plain English: Each fermion mass equals the Higgs scale (v/ 2)
scaled by a power of the fine structure constant (αnf ), with a sectordependent coefficient (Af ) determined by the fermion’s topological
“address” in the CP2 ×S 3 bundle. The exponents are integers or simple
fractions forced by the geometry.

53

CHAPTER 8. NINE MASSES FROM ONE FORMULA

electron (e)
up (u)
down (d)
strange (s)
muon (µ)
charm (c)
tau (τ )
bottom (b)
Observed
DFD predicted

top (t)

10−4

10−3

10−2

10−1

100

101

102

Mass (GeV) — logarithmic scale

Figure 8.1: Nine fermion masses: DFD prediction vs. observation. Blue
bars: measured values. Orange bars: DFD predictions from a single topological formula. Mean error: 1.42% across thirteen orders of magnitude. No
free parameters.

8.3

The Results

Nine charged fermion masses predicted with a mean error of 1.42%. This is
not perfection — but it’s 1.42% across thirteen orders of magnitude, from
one formula, with no continuous parameters.

A mean error of 1.42% across 13 orders of magnitude. From
a single topological formula. With no free parameters.
54

8.3. THE RESULTS

Honest caveat: The CKM and PMNS matrices (which govern how quarks
and neutrinos mix) are predicted in the framework but not yet computed to
full precision. This is ongoing work.

Chapter Summary
The DFD one-liner: The masses of all nine charged fermions — spanning 13 orders of magnitude — follow from one topological formula.
What would confirm: Successful prediction of the CKM and PMNS
mixing matrices from the same framework.
What would break it: Discovery of a new fundamental fermion not
predicted by the CP2 × S 3 index theory.

55

Part IV
The Cosmos

DFD from here to the edge of the observable universe

56

Chapter 9
The Universe Isn’t Accelerating — It
Just Looks That Way
“Not only is the universe stranger than we imagine, it is
stranger than we can imagine.”
— J.B.S. Haldane

9.1

The 1998 Surprise

In 1998, two teams of astronomers made a Nobel Prize–winning discovery:
distant supernovae — the “standard candles” of cosmology — were about
25% fainter than expected. The conclusion: the universe’s expansion is
accelerating. Something was pushing it apart. That something was dubbed
“dark energy.”
But here’s the logic chain: a supernova appears faint → we conclude it’s
farther than expected → we conclude the universe expanded faster than
expected → we invent dark energy to explain it.
DFD asks: what if the first step has another explanation?

57

CHAPTER 9. THE UNIVERSE ISN’T ACCELERATING — IT JUST LOOKS THAT WAY

9.2

What “Faint” Actually Means

A supernova appears faint because it’s far. But there’s another way to appear
faint: if the light has been dimmed — diluted by passing through a medium
with varying refractive properties.
In optics, a medium with a gradually changing refractive index doesn’t
just bend light; it can systematically dilute the flux from a distant source. If
the ψ field has accumulated between us and a distant supernova, the light
will appear dimmer. We’ll infer a greater distance than the true distance.

Lookback time

Supernova (z ≈ 1)

Light dimmed

∆ψ builds up along

by e∆ψ

the light path

Observer
Us (today)

Figure 9.1: The ψ-screen effect. Light from a distant supernova passes
through regions of accumulated ψ field. The light is systematically dimmed,
not because the supernova is farther than expected, but because it passed
through a denser optical medium. Standard cosmology interprets this as
acceleration. DFD interprets it as optics.

9.3

The ψ -Screen

DFD’s key number: ∆ψ(z = 1) = 0.27 ± 0.02. The ψ field has built up by
about 27% between us and objects at redshift 1. This makes objects at
58

9.4. THREE INDEPENDENT MEASUREMENTS THAT MUST AGREE

z = 1 appear about 30% farther than they would in a matter-only universe
— exactly what we observe.

We’re not seeing the universe accelerate. We’re seeing it
through an uneven optical medium.

9.4 Three Independent Measurements That Must Agree
DFD predicts that ∆ψ can be estimated three independent ways:
1. From supernovae: how much dimmer than expected they appear
2. From BAO + lensing: comparing angular diameter distances to luminosity distances
3. From CMB acoustic peaks: subtle direction-dependent shifts in the
peak positions
If DFD is right, all three give the same ∆ψ(n̂) at every direction on the
sky. If they disagree, the mechanism fails.

This is the killer test for our cosmology. Three independent
measurements of the same field. They must agree.

9.5

The Hubble Tension — Resolved

The “Hubble tension” is a 5σ discrepancy: local measurements give H0 ≈ 73
km/s/Mpc; the CMB gives ≈ 68 km/s/Mpc.
59

CHAPTER 9. THE UNIVERSE ISN’T ACCELERATING — IT JUST LOOKS THAT WAY

DFD’s prediction: H0 = 72.09 km/s/Mpc, from the cosmological closure
relation GℏH02 /c5 = α57 .
The ψ-screen explains why the CMB-inferred H0 is biased low: it doesn’t
account for accumulated ψ along the line of sight to the last-scattering
surface.
The Hubble Tension

ΛCDM

DFD

5σ tension. Unexplained.

Resolved. H0 = 72.09 from the

Possible unknown systematic or

α57 relation. CMB bias explained

new physics.

by ψ-screen.

Chapter Summary
The DFD one-liner: Dark energy doesn’t exist. The universe isn’t
accelerating. We’re looking at it through a ψ-screen that dims distant
light.
What would confirm: The three ∆ψ estimators (SNe, BAO+lensing,
CMB) agree in a model-independent reconstruction.
What would break it: No correlation between reconstructed ∆ψ(n̂)
and foreground large-scale structure.

60

Chapter 10
The CMB — Sound Frozen in Light
10.1

The Oldest Light in the Universe

About 380,000 years after the Big Bang, the universe cooled enough for
electrons to combine with protons. Space became transparent. The light
released at that moment is still traveling today — we call it the Cosmic
Microwave Background (CMB). It’s the most precisely measured blackbody
radiation in history: temperature 2.725 K, with fluctuations of one part in
100,000.

10.2

The Acoustic Peaks

The fluctuations form a specific pattern of peaks. The first peak is at angular
scale ℓ ≈ 220. The second at ℓ ≈ 538. The third at ℓ ≈ 810.
The ratio of the first to second peak heights, R ≈ 2.34, is sensitive to the
baryon-to-photon ratio. Standard cosmology says you need dark matter to
suppress the even peaks and get R right.

10.3

DFD’s CMB

DFD predicts R = 2.34 from baryon loading alone — no dark matter component. The first peak location is set by ψ-lensing: ∆ψ = 0.30 shifts ℓ1 to 220,
61

CHAPTER 10. THE CMB — SOUND FROZEN IN LIGHT

exactly where it’s observed.
Honest caveat: Full CMB power spectrum matching (all the peaks, the
damping tail, polarization) is a program item, not yet complete. DFD matches
the gross features; detailed fitting is ongoing work.

Chapter Summary
The DFD one-liner: The CMB acoustic peaks — often cited as proof
of dark matter — can be explained by baryon loading and ψ-lensing
alone.
What would confirm: Full DFD CMB power spectrum code producing
a fit comparable to ΛCDM.
What would break it: Detailed peak structure that fundamentally
requires a pressureless dark component and cannot be replicated by
any ψ-screen configuration.

62

Part V
The Verdict

How we’ll know if DFD is right or wrong

63

Chapter 11
Atomic Clocks — The Most Important
Experiment You’ve Never Heard Of
11.1

The World’s Most Precise Instruments

Modern optical atomic clocks are accurate to 1 second in 30 billion years.
They work by locking a laser to a specific atomic transition — the quantum
“tick” of the atom — and counting the oscillations.
At this precision, you can detect the gravitational redshift from moving
your clock from the floor to a table. These instruments are sensitive enough
to test DFD.

11.2

What GR Predicts for Clocks

In GR, a clock at lower gravitational potential runs slower. Crucially, this
effect is universal: every clock of every kind, at the same location, shifts by
the same fractional amount. This is called Local Position Invariance (LPI).
GR’s prediction for any anomalous clock dependence: ξ = 0. Exactly
zero. Always.

65

CHAPTER 11. ATOMIC CLOCKS — THE MOST IMPORTANT EXPERIMENT YOU’VE
NEVER HEARD OF

11.3

What DFD Predicts — And Why It’s Different

In DFD, the ψ field couples to matter through the fine structure constant
α. Different atoms have different sensitivity to α, quantified by a number
SAα . As ψ changes with altitude, α effectively shifts — and different clocks
respond differently.

2.83

α (sensitivity to α)
SA

2
1
6 · 10−2

0

8 · 10−3

−5
−5.95

S
HF
Cs

Hm

a

ser

opt
Sr

+

Al

+ E2

Yb

Largest
contrast!

+ E3

Yb

Clock species

Figure 11.1: Different clocks, different sensitivities. Each atomic species
responds differently to changes in α. DFD predicts that comparing clocks
with very different SAα values — especially Yb+ E3 (−5.95) vs. Al+ (+0.008)
— will reveal species-dependent gravitational coupling.

The DFD prediction: the ratio of two different clock species should shift
as you move to different gravitational potentials. The shift: KA = kα · SAα ,
where kα = α2 /(2π) ≈ 8.5 × 10−6 .
The falsification test: measure ξLPI . GR predicts ξ = 0. DFD predicts
ξ ≈ 1–2.
66

11.4. THE CAVITY TEST — EVEN CLEANER

This is a binary discriminator. ξ ̸= 0 falsifies GR. ξ = 0
falsifies DFD. There’s no hiding.

11.4

The Cavity Test — Even Cleaner

Compare a cavity resonance frequency (photon sector) to an atomic frequency (matter sector) as height changes. The cavity depends on the speed
of light. The atom depends on electronic structure. In DFD, they couple to
ψ differently.

Put one cavity clock and one atomic clock in an elevator.
Watch the ratio as you ascend. GR: no change. DFD: measurable drift at 10−5 level.
Labs that could run this experiment today: JILA (Jun Ye’s group), PTB
(Germany), NIST, NPL.

Chapter Summary
The DFD one-liner: Co-located atomic clocks of different species,
compared at different altitudes, will either confirm or kill DFD in a
single measurement.
What would confirm: ξ ̸= 0 at the predicted magnitude, with species
dependence matching SAα values.
What would break it: ξ = 0 at 10−2 precision.

67

Chapter 12
One Test Already Confirmed — The
Solar Corona
12.1

The Solar Wind Problem

The Sun’s corona — its outer atmosphere — is millions of degrees hot,
while the surface below is only about 6,000 K. Solar wind ions stream
outward at hundreds of kilometers per second. The SOHO spacecraft’s
UVCS spectrometer measured the outflow characteristics of different ion
species.

12.2

The DFD Prediction

Standard solar physics predicts that the ratio of spectral line widths for
two ion species transiting the corona should be Γ ≈ 1. DFD predicts a
double-transit effect: the ψ field modifies ion outflow differently from
photon propagation, giving Γ = 4.
This is not a subtle effect. It’s a factor-of-four deviation.

12.3

The Measurement

Analysis of SOHO/UVCS archival data:
68

12.3. THE MEASUREMENT

Γ (line width ratio)

6
Γ=4

Observed: 4.4 ± 0.9

4

3.7σ from
standard

2

Γ=1

0
DFD

Standard

Figure 12.1: The UVCS result. Standard physics predicts Γ = 1. DFD
predicts Γ = 4. The SOHO/UVCS data give Γ = 4.4 ± 0.9 — within 0.4σ
of DFD and 3.7σ away from standard. This is the first confirmed DFD
prediction.

This is the first test where DFD and standard physics make
dramatically different predictions, and the data has spoken.
Honest caveat: This analysis has been submitted to Solar Physics journal. It
has not yet completed peer review. Independent replication with different
datasets would be decisive.

69

CHAPTER 12. ONE TEST ALREADY CONFIRMED — THE SOLAR CORONA

Chapter Summary
The DFD one-liner: DFD predicted a factor-of-four enhancement in
solar coronal line-width ratios. The observation matches at 0.4σ.
What would confirm: Independent analysis of additional UVCS
datasets. Replication with other solar spectrometers.
What would break it: Revised analysis showing Γ ≈ 1 after accounting for previously neglected systematic effects.

70

Chapter 13
How to Break DFD — The Falsification
Map
“A theory that cannot be refuted by any conceivable event is
non-scientific.”
— Karl Popper

13.1

Why Falsifiability Matters

A scientific theory must be capable of being proven wrong. The reason:
unfalsifiable theories can accommodate any observation after the fact. DFD’s
commitment: we specify in advance exactly what observations would kill
the theory.

13.2

The Five Binary Discriminators

13.3

Direct Dark Matter Detection

If a dark matter particle with consistent properties is directly detected in
laboratory experiments — same mass, same coupling, reproducible across
multiple experiments — DFD would need fundamental revision. DFD doesn’t
71

CHAPTER 13. HOW TO BREAK DFD — THE FALSIFICATION MAP

Test

Standard

DFD

“DFD is Wrong”

LPI (cavity–atom)

ξ=0

ξ ≈ 1–2

ξ = 0 at 10−2

Clock

Universal

Speciesdependent

GW speed cT

c

c

No species dependence
cT ̸= c at 10−15

SPARC / RAR

Needs dark matter

Baryons alone

Deviations > 3σ

ψ -screen ∆ψ

N/A

Correlates
structure

No correlation

couplings

KA

with

Figure 13.1: The falsification map. Five tests, five binary outcomes. Each
row is a go/no-go check for DFD.

predict that no particle beyond the Standard Model exists. It predicts that
whatever exists is not responsible for galaxy rotation curves.

13.4

An Invitation

Every scientist who reads this, every experimental team, every theorist
looking for a flaw — we invite you. The best outcome if DFD is wrong: we
find out quickly, and physics moves on with sharper understanding. The
best outcome if DFD is right: physics changes forever.

We have told you exactly how to break this theory. Now we
invite you to try.
72

13.4. AN INVITATION

Chapter Summary
The DFD one-liner: DFD is the rare theory that publishes its own
death warrants.
What would confirm: Surviving every test in this chapter.
What would break it: Failing any single one.

73

Part VI
The Deeper Picture

If DFD is right, what does it mean?

74

Chapter 14
A Universe Without Dark Inventory
14.1

The End of the Dark Sector

If DFD is confirmed experimentally, the cosmic inventory changes fundamentally. No cold dark matter particles. No cosmological constant. No
120-order-of-magnitude fine-tuning problem.
What exists: ordinary matter, the ψ field, and the topology of CP2 × S 3 .

14.2

The Standard Model from Geometry

If DFD is right, the Standard Model gauge group SU(3) × SU(2) × U(1) —
the three forces of particle physics — arises from a (3, 2, 1) partition of the
CP2 × S 3 bundle structure. Three generations of fermions from index theory
on the manifold.

The fact that there are exactly three generations of quarks
and leptons — not two, not four — would be a theorem in
topology.

75

CHAPTER 14. A UNIVERSE WITHOUT DARK INVENTORY

14.3

Strong CP Without the Axion

One of the deepest puzzles in particle physics: why doesn’t the strong nuclear
force violate CP symmetry? The Standard Model allows it. Experiment shows
it doesn’t. The usual solution: a hypothetical particle called the axion, never
detected.
DFD: θ̄ = 0 to all loop orders. The topology forces it. No new particle
needed.

Another 50-year-old problem solved by the same geometry.

14.4

What Remains Unknown

Honest accounting of open problems:

1. Full CMB power spectrum matching (P (k)) — program item, not yet
complete

2. Loop corrections in the ψ–gauge coupled system — not yet computed

3. The DFD analog of Hawking radiation — unclear

4. Neutrino masses and PMNS matrix — partial framework

5. The physical interpretation of ψ itself — what is the medium?
76

14.4. WHAT REMAINS UNKNOWN

Chapter Summary
The DFD one-liner: If confirmed, DFD eliminates the dark sector,
derives the Standard Model from topology, and solves the strong CP
problem — from a single geometric framework.
What would confirm: Experimental verification of the clock predictions plus successful CMB power spectrum fitting.
What would break it: A competing framework that matches DFD’s
successes without requiring specific topology.

77

Chapter 15
What Is the Medium?
15.1

The Old Ether Problem

Before Einstein, physicists assumed light needed a medium — the “luminiferous ether.” The Michelson-Morley experiment of 1887 showed no such
medium exists. Einstein resolved the paradox by abandoning absolute space
and time.
DFD seems to bring back a medium. Are we regressing?

15.2

The Difference

The old ether was a preferred reference frame — it was supposed to tell you
whether you’re “really moving.” DFD’s ψ field does not define a preferred
frame. Lorentz invariance is preserved. The optical metric is not a flat
background with a distinguished observer.
What ψ is: a scalar degree of freedom that encodes the local density
of the CP2 × S 3 microsector — a geometric object, not an ether. The way
temperature is an emergent description of atomic motion, ψ is an emergent
description of the underlying geometry.

78

15.3. THE OPEN QUESTION

15.3

The Open Question

What is the ψ field made of, at the deepest level? What are its “atoms”?
DFD’s current answer: it’s emergent from the microsector geometry. The
deeper question remains open. And that’s exactly how science should work.

The greatest scientific theories don’t end questions. They
replace one mystery with a deeper, better-posed one.

Chapter Summary
The DFD one-liner: DFD’s ψ field is not the old ether. It’s a geometric
degree of freedom that preserves Lorentz invariance while providing
a physical mechanism for gravity.
What would confirm: A microscopic derivation of ψ from quantum
geometry.
What would break it: Detection of a preferred frame effect in precision experiments — which would break DFD and GR.

79

Appendix A
The Equations — A Glossary
Every DFD equation in one place, each with its plain-English translation.
Equation

What it means

n = eψ

The refractive index of space. Where
ψ is larger, light travels slower.

c1 = c e−ψ

The local (one-way) speed of light.
Slower near mass.

c2

a = 2 ∇ψ

Things accelerate toward stronger ψ.
This is gravity.

x
µ(x) = 1+x

The throttle function. Full power for
strong gravity; reduced for weak gravity. Derived from S 3 topology.


i
h 
|∇ψ|
ρ
∇· µ a∗ ∇ψ = − 8πG
c2

The master equation. Matter sources
ψ; ψ drives acceleration.

α−1 = 137.036

The fine structure constant. Derived
from Chern-Simons quantization on

√
a∗ = 2 α c H0

CP2 × S 3 .
The crossover acceleration. Derived,
not fitted.

GℏH02 /c5 = α57

The cosmological closure relation.
Links gravity, quantum mechanics, and
expansion.
80

Appendix B

The Evidence — A Summary Table
81

APPENDIX B. THE EVIDENCE — A SUMMARY TABLE

Observable

DFD Predicts

Observed

Agreement

α−1

137.036

137.036

< 0.001%

Status

Derived
Higgs VEV

246.09 GeV

246.22 GeV

0.05%
Derived

H0

72.09 km/s/Mpc

72.6 ± 2.0

0.3σ

UVCS Γ

4.0

4.4 ± 0.9

0.4σ

Derived
Confirmed
Electron mass

0.511 MeV

< 0.1%

0.511 MeV

Derived
CMB peak ratio R

2.34 ± 0.02

2.34

exact
Derived

MOND a0

1.2 × 10

−10

∼ 1.2 × 10

−10

match
Derived

PPN γ, β

1, 1

1, 1

exact
Matched

GW speed cT

c

c

−15

< 10

Matched
SPARC 175 galaxies

< 5% residuals

< 5%

confirmed
Confirmed

Clusters (16/16)

0.98 ± 0.05

data

< 10%
Confirmed

LPI ξ

≈ 1–2

—

—
Pending

Clock KA

species-dep.

—

—

∆ψ correlation

yes

—

—

Pending
Pending
Full CMB P (k)

in progress

—

—
Open

82

Appendix C
The Falsification Map
LPI Clock Test

ξ =?

Clock Couplings

KA =?

DFD
falsified

ξ=0

SPARC Galaxies
175 fits

ψ -screen
∆ψ(n̂)

Dark Matter
Detection

83

ξ ̸= 0

DFD
survives

Appendix D

For the Skeptical Physicist

If you’re a professional physicist and you’ve made it this far, here’s the map
to the full technical derivations.
84

This Book

Technical Paper (v3.1)

Chapter 2 (Optics)

Section 2: Formalism; Section 3:
Well-posedness

Chapter 3 (Field Eq.)

Section 2; Appendix N (µ(x) derivation)

Chapter 4 (PPN)

Section 4: PPN Parameters

Chapter 5 (Galaxies)

Section 7: Galactic Dynamics; Appendix I

Chapter 6 (Topology)

Appendix K; Appendix N

Chapter 7 (α)

Section 8C: Convention-Locked α;
Appendix K

Chapter 8 (Masses)

Appendix Y: Finite Yukawa Operators

Chapter 9 (ψ-Screen)

Section 12: Cosmology; Appendix
O

Chapter 10 (CMB)

Section 12.3; P (k) Confrontation

Chapter 11 (Clocks)

Section 10: Cavity-Atom; Appendix
P

Chapter 12 (UVCS)

Section 11A: Solar Corona; Appendix M

Chapter 13 (Falsifica- Section 14: Open Problems; Aption)

pendix W

Full paper: Density Field Dynamics: A Unified Review (v3.1)
DOI: 10.5281/zenodo.18066593

85

Appendix E
Further Reading
The technical paper:
Gary Alcock, Density Field Dynamics: A Unified Review, v3.1 (2026).
DOI: 10.5281/zenodo.18066593
Background reading:
Richard P. Feynman, QED: The Strange Theory of Light and Matter (1985)
Mordehai Milgrom, A Modification of the Newtonian Dynamics (1983)
Clifford M. Will, Theory and Experiment in Gravitational Physics (2018)
Stacy S. McGaugh, The Baryonic Tully-Fisher Relation (2005)
Experimental context:
Jun Ye et al., optical lattice clock papers (JILA, various)
McGaugh et al., SPARC: Spitzer Photometry and Accurate Rotation Curves
(2016)
SOHO/UVCS instrument and data documentation (ESA/NASA)

“The universe is not only queerer than we suppose,
but queerer than we can suppose.” — J.B.S. Haldane

86

