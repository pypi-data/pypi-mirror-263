"""
--------------------------------------------------------------------------
Air Force Research Laboratory (AFRL) Autonomous Capabilities Team (ACT3)
Safe Autonomy Dynamics.

This is a US Government Work not subject to copyright protection in the US.

The use, dissemination or disclosure of data in this file is subject to
limitation or restriction. See accompanying README and LICENSE for details.
---------------------------------------------------------------------------

Stanley Bak
Python GCAS F - 16
dldr function
"""

import numpy as np

from safe_autonomy_dynamics.external.aerobench.util import fix, sign


def dldr(alpha, beta):
    'dldr function'

    a = np.array(
        [
            [.005, .017, .014, .010, -.005, .009, .019, .005, -.000, -.005, -.011, .008], [
                .007, .016, .014, .014, .013, .009, .012, .005, .000, .004, .009, .007
            ], [.013, .013, .011, .012, .011, .009, .008, .005, -.002, .005, .003, .005], [
                .018, .015, .015, .014, .014, .014, .014, .015, .013, .011, .006, .001
            ], [.015, .014, .013, .013, .012, .011, .011, .010, .008, .008, .007, .003], [
                .021, .011, .010, .011, .010, .009, .008, .010, .006, .005, .000, .001
            ], [.023, .010, .011, .011, .011, .010, .008, .010, .006, .014, .020, .000]
        ],
        dtype=float
    ).T

    s = .2 * alpha
    k = fix(s)
    if k <= -2:
        k = -1

    if k >= 9:
        k = 8

    da = s - k
    l = k + fix(1.1 * sign(da))  # noqa: E741
    s = .1 * beta
    m = fix(s)

    if m <= -3:
        m = -2

    if m >= 3:
        m = 2

    db = s - m
    n = m + fix(1.1 * sign(db))
    l = l + 3  # noqa: E741
    k = k + 3
    m = m + 4
    n = n + 4
    t = a[k - 1, m - 1]
    u = a[k - 1, n - 1]

    v = t + abs(da) * (a[l - 1, m - 1] - t)
    w = u + abs(da) * (a[l - 1, n - 1] - u)

    return v + (w - v) * abs(db)
