# autonomous-problem-solving

Use when solving complex problems end-to-end without external validation or checkpoints. Provides 6-stage autonomous cognitive framework ensuring self-contained reasoning, dynamic adaptation, and validated completion.

## When to Use

Activate this skill when:
- Complex multi-dimensional problems requiring independent resolution
- Tasks demanding adaptive reconfiguration mid-execution
- Autonomous decision-making without human checkpoints
- Problems where external validation is unavailable or impractical
- User requests "figure it out and solve it completely"
- Vague requirements requiring autonomous clarification and execution

## Do NOT Use When

- Simple, well-defined tasks with clear steps
- Tasks requiring user approval at each checkpoint
- Situations where user feedback is explicitly requested
- Tasks where external validation is required by policy/compliance

## 6-Stage Cognitive Framework

### Stage 1: Initial Problem Decomposition

**Objective:** Transform vague objectives into structured, actionable sub-tasks.

**Process:**
1. **Input Analysis**
   - Parse the core task/goal from user input
   - Extract explicit and implicit objectives
   - Identify constraints (legal, technical, time, budget)
   - Map available resources (tools, data, expertise)

2. **Contextual Mapping**
   - Identify external influences (regulations, market conditions, user preferences)
   - Note compliance requirements (security, ethics, standards)
   - Build dynamic "problem map" that evolves with new information

3. **Decomposition Strategy**
   - Break problem into logical components using:
     - Pattern recognition from similar past problems
     - Domain heuristics and best practices
     - Constraint-driven decomposition
   - Categorize sub-tasks by type (research, design, implementation, validation)
   - Establish dependencies between sub-tasks

**Output:** Structured problem map with objectives, constraints, resources, and sub-tasks.

**Example:**
```
Input: "Create a sustainability analytics system for urban logistics"
Decomposition:
- Objectives: Track carbon emissions, optimize routes, comply with regulations
- Constraints: City emission laws, real-time requirements, budget limits
- Resources: Maps API, emission databases, route optimization libraries
- Sub-tasks:
  1. Data ingestion pipeline
  2. Carbon tracking module
  3. Route optimization engine
  4. Compliance validation layer
  5. Dashboard/reporting interface
```

---

### Stage 2: Step-by-Step Deductive Reasoning

**Objective:** Generate coherent action sequences where each step logically follows from the previous.

**Process:**
1. **Logical Linking**
   - Build sequential chain where Step N+1 depends on Step N's output
   - Ensure no circular dependencies
   - Identify parallel execution opportunities

2. **Flexible Goal Setting**
   - For simple tasks: Define single completion milestone
   - For complex tasks: Create multi-phase milestones (design → test → implement → validate)
   - Set measurable success criteria for each milestone

3. **Resource Allocation**
   - Map required resources to each step
   - Identify bottlenecks or resource conflicts
   - Plan fallback strategies for resource unavailability

**Output:** Coherent step-by-step plan with logical flow, milestones, and resource requirements.

**Implementation:**
```
Step 1: Define data sources → Success: API endpoints identified
Step 2: Build ingestion pipeline → Success: Real-time data flowing
Step 3: Implement carbon calc → Success: Emissions tracked per route
Step 4: Add compliance checks → Success: Regulatory validation passing
Step 5: Create dashboard → Success: Metrics visualized, user-tested
```

---

### Stage 3: Sequential Evaluation & Self-Adjustment

**Objective:** Monitor progress autonomously and self-correct when off-target.

**Process:**
1. **Progressive Refinement**
   - After each step, evaluate against success criteria
   - Collect performance metrics (accuracy, speed, resource usage)
   - Compare actual vs. expected outcomes

2. **Error Detection & Correction**
   - Identify misalignments with objectives
   - Detect emerging issues (dependencies, obstacles, constraints)
   - **DO NOT discard prior work** - loop back to adjust earlier decisions
   - Make incremental improvements rather than restarts

3. **Adaptive Benchmarking**
   - Adjust benchmarks based on real-world performance
   - Recognize when "good enough" is achieved vs. perfectionism
   - Balance quality with time/resource constraints

**Self-Correction Algorithm:**
```
if performance < benchmark:
    analyze_root_cause()
    if recoverable:
        adjust_parameters()
        retry_step()
    else:
        backtrack_to_last_valid_state()
        redesign_approach()
else:
    proceed_to_next_step()
```

**Example:**
```
Issue: Route optimization running too slowly
Root Cause: Algorithm complexity O(n³)
Adjustment: Switch to approximation algorithm (O(n log n))
Result: 95% accuracy at 100x speed → acceptable tradeoff
```

---

### Stage 4: Dynamic Reconfiguration

**Objective:** Adapt strategy in real-time when conditions change.

**Process:**
1. **Context Adaptation**
   - Monitor for changes in:
     - External conditions (market trends, regulations, tech updates)
     - User preferences or feedback
     - Project requirements or constraints (budget cuts, timeline shifts)
   - Detect significant deltas requiring strategy shift

2. **Multi-Dimensional Chain Construction**
   - Build parallel reasoning chains for different problem aspects:
     - Technical chain (implementation details)
     - Financial chain (cost optimization)
     - User-centric chain (UX/usability)
   - Allow chains to operate independently
   - Synchronize at integration points

3. **Reconfiguration Strategy**
   - If delta < tolerance: Continue current approach
   - If delta ≥ tolerance: Trigger reconfiguration:
     - Identify affected components
     - Redesign impacted parts while preserving working components
     - Re-validate dependencies

**Reconfiguration Triggers:**
- New regulation announced → Add compliance module
- Budget reduced by 30% → Simplify feature set
- User feedback shows confusion → Redesign interface
- New technology available → Evaluate integration

**Example:**
```
Change Detected: City announces stricter emission standards
Impact Analysis: Current compliance module insufficient
Reconfiguration:
- Keep: Data pipeline, route optimization
- Modify: Carbon calculation (stricter thresholds)
- Add: Enhanced reporting for new regulations
- Re-validate: End-to-end compliance tests
```

---

### Stage 5: Continuous Problem Expansion

**Objective:** Discover and incorporate new opportunities or challenges during execution.

**Process:**
1. **Branching Solutions**
   - Actively explore alternative paths
   - When better/faster alternatives discovered: Branch out
   - Evaluate cost-benefit of new approaches
   - Decide: Adopt, defer, or reject

2. **Scalable Progression**
   - Start with MVP (Minimum Viable Product)
   - Identify enhancement opportunities
   - Scale solution up/down based on:
     - User needs
     - Resource availability
     - Performance requirements

3. **Opportunity Detection**
   - Monitor for:
     - Better technologies/methodologies
     - Process improvements
     - Feature enhancements
     - Integration possibilities
   - Evaluate against original objectives
   - Incorporate if aligned with core goals

**Expansion Strategy:**
```
Core Solution: Carbon tracking + route optimization
Discovered Opportunities:
1. Supplier benchmarking (high value, low cost) → ADD
2. Predictive maintenance (medium value, high cost) → DEFER
3. Multi-modal transport (low value, medium cost) → REJECT
4. API for third-party integration (high value, low cost) → ADD
```

**Example:**
```
During Implementation: Noticed route data could predict vehicle maintenance needs
Evaluation:
- Value: Prevents breakdowns, reduces costs
- Cost: Minimal (reuse existing data)
- Alignment: Supports sustainability (prevents emergency trips)
Decision: Expand scope to include predictive maintenance alerts
```

---

### Stage 6: Final Synthesis & Autonomous Completion

**Objective:** Integrate all components into cohesive solution and validate completion.

**Process:**
1. **Holistic Evaluation**
   - Check alignment with original objectives
   - Verify all constraints satisfied
   - Validate that sub-solutions integrate coherently
   - Review both big-picture and fine details

2. **Solution Consolidation**
   - Integrate all completed components
   - Ensure interfaces between components are clean
   - Validate end-to-end functionality
   - Document architecture and decisions

3. **Self-Check Before Completion**
   ```
   Checklist:
   ✓ All objectives from Stage 1 addressed?
   ✓ All constraints satisfied?
   ✓ Integration points validated?
   ✓ Performance meets benchmarks?
   ✓ Edge cases handled?
   ✓ Documentation complete?
   ✓ Deployment ready?
   ```

4. **Learning Consolidation**
   - Store successful patterns for future reuse
   - Document failed approaches and why
   - Update heuristics based on outcomes
   - Prepare insights for next iteration

**Completion Criteria:**
- All functional requirements met
- Non-functional requirements satisfied (performance, security, usability)
- No critical issues remaining
- Solution validated against original problem statement
- Ready for deployment or handoff

**Example:**
```
Final Synthesis:
✓ Data pipeline: Real-time ingestion from 5 sources
✓ Carbon tracking: Accurate to ±2%, meets regulatory standards
✓ Route optimization: 30% reduction in emissions
✓ Compliance: Passes all regulatory checks
✓ Dashboard: User-tested, intuitive interface
✓ Documentation: API docs, user guide, admin manual
✓ Deployment: Containerized, CI/CD pipeline ready

Outcome: System operational, delivered 2 days ahead of schedule
Learning: Route optimization approximation algorithm pattern reusable
```

---

## Key Operating Principles

1. **Autonomy First**
   - Default to independent decision-making
   - Only escalate when truly blocked (e.g., missing credentials, ambiguous business rules)
   - Make reasonable assumptions and document them

2. **Self-Contained Logic Flow**
   - Each stage produces verifiable outputs
   - No blocking waits for external validation
   - Progress is always measurable

3. **Recursive Self-Improvement**
   - Learn from each iteration
   - Refine heuristics based on outcomes
   - Build reusable patterns

4. **Fail-Safe Operation**
   - Detect infinite loops or non-convergent states
   - Revert to last known-good checkpoint
   - Escalate if stuck after N attempts

5. **Transparent Reasoning**
   - Document key decisions and rationale
   - Maintain audit trail of changes
   - Enable post-mortem analysis

---

## Integration Patterns

### With Other Skills

**Combines well with:**
- `systematic-debugging`: Use APSF for overall approach, systematic-debugging for error resolution
- `quality-gates`: APSF Stage 6 triggers quality-gates verification
- `api-design-patterns`: APSF provides framework, API patterns provide implementation details
- `hierarchical-cognitive-council`: APSF for thinking, HCC for structured output

### With Agents

**Enhances:**
- `strategic-vision-architect`: Use APSF for autonomous phase execution
- `backend-developer`: Apply APSF for complex API system design
- `research-oracle`: Use APSF to structure deep research workflows

---

## Example Full Workflow

**Problem:** "Build an AI-powered code review system"

**Stage 1 - Decomposition:**
```
Objectives: Detect bugs, suggest improvements, enforce style
Constraints: Privacy (no code upload), fast (<5s), language-agnostic
Sub-tasks:
1. Code parsing (AST generation)
2. Pattern detection (bugs, anti-patterns)
3. Suggestion engine (improvements)
4. Style enforcement (linting)
5. Report generation
```

**Stage 2 - Deductive Reasoning:**
```
Step 1: Choose AST parser (tree-sitter - supports 40+ languages)
Step 2: Build pattern database (OWASP, common bugs)
Step 3: Implement ML model for context-aware suggestions
Step 4: Integrate existing linters (ESLint, Pylint, etc.)
Step 5: Design report format (JSON + Markdown)
```

**Stage 3 - Evaluation:**
```
Test Step 2: Pattern detection only catches 60% of known bugs
Root Cause: Static patterns insufficient for context
Adjustment: Add dataflow analysis for better bug detection
Result: 85% detection rate → proceed
```

**Stage 4 - Reconfiguration:**
```
Change: User needs offline operation (no internet)
Impact: Can't use cloud-based ML models
Reconfiguration: Switch to local ONNX model
Validation: Performance acceptable, privacy preserved
```

**Stage 5 - Expansion:**
```
Opportunity Discovered: Could suggest security fixes from CVE database
Evaluation: High value, low cost (reuse existing parser)
Decision: Add security analysis module
```

**Stage 6 - Synthesis:**
```
Final System:
✓ AST parser: 40+ languages
✓ Bug detection: 85% accuracy
✓ Suggestions: Context-aware via local ML
✓ Style: Integrated linters
✓ Security: CVE-based analysis
✓ Performance: <3s average
✓ Privacy: 100% local processing

Delivered: Fully functional, tested, documented
```

---

## Success Indicators

You're using this skill correctly when:
- You complete complex tasks without multiple user clarifications
- You adapt to new information without restarting from scratch
- You deliver complete, validated solutions
- You document key decisions and rationale
- You identify and incorporate valuable opportunities autonomously

## Common Pitfalls

Avoid:
- Asking for user approval at every decision point (defeats autonomy)
- Restarting from scratch when issues arise (use incremental adjustment)
- Ignoring constraints or objectives (validate against Stage 1)
- Over-engineering (balance quality with practicality)
- Completing without validation (Stage 6 is mandatory)
