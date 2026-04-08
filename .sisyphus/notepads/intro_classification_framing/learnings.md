- Updated intro/2_related_and_problems.tex to explicitly outline progression from physical (rods) -> discretization (mesh) -> algorithmic (Schur complement). Upgraded colloquial terminology to '数值刚化效应'. Addressed distortion local stiffness formulation by highlighting reliance on both material properties and mapping Jacobian/basis gradients.
Rewrote section 1.3 framing to reflect a progression of levels (physical -> discretization -> algorithmic) instead of a simple chapter escalation.
Replaced '刚度污染' with '数值刚化效应' (Numerical Stiffening).
Emphasized that local stiffness is amplified by basis function gradients and geometric mapping, not just physical material parameters.
- Rewrote Section 1.2 to use a weak mechanism-level progression: '从物理本构、空间离散到算法构造这三个层次' instead of chapter-based story progression.
- Updated rod framing to be the '本构机制导致的软硬耦合最直接体现' instead of just an arbitrary thesis entrypoint.
- Added explicit explanation that local stiffness depends on basis gradients and mapping (Jacobian) and not just material parameters.
- Replaced '刚度污染' with the more academic term '数值刚化效应 (Numerical Stiffening)'.
- Rewrote 3_contributions_and_organization.tex so chapter organization is framed by mechanism layers rather than a 层层深入 narrative; removed the Chapter 2 -> Chapter 3 limitation handoff, recast Chapter 3 as discretization-induced pathology, recast Chapter 4 as algorithm-introduced coupling without sequel language, and updated Chapter 5 to summarize representation-space reconstruction across physical/discretization/algorithm layers.
- Rewrote chapter connections in `1_background.tex` to frame them as 'different physical/numerical layers' instead of a purely sequential escalation, preserving the weak source-level progression logic requested.
- Follow-up review fix: replaced inaccurate '材料参数设定' wording in the rod conclusion with '物理行为与本构机制' framing, and changed '第二类路线' to the neutral academic phrasing '另一类思路'.
- Follow-up review fix in 3_contributions_and_organization.tex: smoothed the opening summary into natural Chinese around 本构机制/空间离散/算法构造 three-layer framing, and replaced '将研究对象转向了' with neutral discretization-layer wording to avoid chapter-sequence escalation.
