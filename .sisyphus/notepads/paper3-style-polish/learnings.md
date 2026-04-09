# Style Baseline and Anti-Pattern Table

## Original English Style Baseline
- **Tone:** Objective, precise, academic.
- **Diction:** Standard scientific terminology (e.g., "Modal analysis", "Krylov subspace methods", "ill-conditioning", "Component Mode Synthesis").
- **Sentence Structure:** Direct and logical (e.g., "While global solvers... face critical scalability bottlenecks. First... Second...").
- **Claims:** Specific and substantiated (e.g., "offers order-of-magnitude speedups in reanalysis").

## Chinese Thesis Current State (Anti-Patterns)
The translation has drifted into highly stylized, overly emotional, and colloquial phrasing that is inappropriate for a formal PhD thesis.

| Category | English Original | Chinese Translation | Issue / Anti-Pattern |
| :--- | :--- | :--- | :--- |
| **Over-literary Diction** | "ill-conditioning" | "病态条件数积累引发的极端迟钝迭代" | Uses overly dramatic words ("极端迟钝", "海量", "狂飙"). Target: 严谨、朴实 (e.g., "条件数病态导致的迭代缓慢"). |
| **Inflated Rhetoric** | "critical scalability bottlenecks" | "不可跨越的浩瀚天堑与最致命瓶颈" | Overblown metaphors ("天堑", "致命", "巨兽", "毒瘤"). Target: 朴实 (e.g., "严重的扩展性瓶颈"). |
| **Overlong Sentences** | "Modal analysis... is a fundamental tool..." | "前两章分别从显式几何法则约束以及局部底层离散形函数畸变这两个切面层级，剥析了物理模拟体系中由局部高频硬核干扰所引爆的时间积分步缩短与空间离散矩阵条件数病态难题，并成功演示了如何通过改写、定制系统表示与解构空间底层映射，自源头将不良数值刚度彻底剥离以逆转乾坤的解题哲思。" | Run-on sentences packing too many modifiers and dramatic flair ("逆转乾坤的解题哲思"). Target: Concise, clear sentences. |
| **Vague Macro Claims** | "this approach further improves the efficiency..." | "全面展示我们成果狂飙突破 3 个甚至更大量的精度进阶数量级提升跨度优势" | Claims are phrased like marketing copy ("狂飙突破", "跃升级的精度赋能") rather than objective scientific results. Target: Specific, measurable claims. |
| **Colloquialisms** | "The substructure eigenmodes from the two different partitions..." | "这头系统巨兽被大刀阔斧分割成了多块小区域子结构后" | Unprofessional imagery ("这头系统巨兽", "大刀阔斧", "像填鸭般疯狂补充"). Target: Formal academic language. |

## Stage 2 Rewrite Constraints
1.  **Remove Emotional & Dramatic Language:** Eliminate words like "狂飙", "天堑", "致命", "巨兽", "毒瘤", "逆转乾坤", "完美圆融", "惊艳".
2.  **Simplify Sentence Structures:** Break down overlong sentences. Ensure one main idea per sentence.
3.  **Use Standard Academic Terminology:** Stick to accepted Chinese translations for technical terms (e.g., "ill-conditioning" -> "病态", "scalability bottleneck" -> "可扩展性瓶颈", "substructures" -> "子结构").
4.  **Objective Tone:** Present results and methods objectively without marketing-style exaggeration.
5.  **Direct Mapping:** Ensure the Chinese text maps directly to the logical flow of the English original without adding interpretive, poetic flair.
