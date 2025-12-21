# hierarchical-cognitive-council

Use when producing audited, research-intensive deliverables requiring hierarchical structure, deep verification, and quality gates. Ensures outputs have executive summaries, nested details, cited evidence, and pass multi-loop validation before publication.

## When to Use

Activate this skill when:
- Creating research-heavy deliverables (reports, analyses, strategic plans, whitepapers)
- Compliance-critical or audited outputs required
- Complex projects needing nested hierarchical structure
- Work requiring deep research with chained, multi-source searches
- Quality-critical outputs demanding verification loops
- User requests "comprehensive analysis," "full report," or "audit-ready deliverable"
- Outputs will be reviewed by stakeholders, executives, or regulators

## Do NOT Use When

- Quick, informal responses needed
- Simple tasks with no research requirements
- Time-sensitive outputs where thoroughness is secondary
- Internal drafts or working documents
- User explicitly requests "brief summary" or "quick answer"

## Core Principles

### 1. Hierarchical Presentation

**Objective:** Structure information for progressive disclosure - executives see summaries, specialists see details.

**Structure Pattern:**
```markdown
# Executive Summary
[2-3 paragraphs: key findings, recommendations, impact]

## Key Findings
- [Bullet point 1]
- [Bullet point 2]
- [Bullet point 3]

## [Section 1: High-Level Topic]

### [Subsection 1.1: Specific Area]
[Detailed content with evidence]

#### [Sub-subsection 1.1.1: Fine Detail]
[Granular analysis]

- Supporting point A
- Supporting point B

### [Subsection 1.2: Another Specific Area]
[Detailed content]

## [Section 2: Another High-Level Topic]
...

## Recommendations
1. [Action item with rationale]
2. [Action item with rationale]

## Appendices
### Appendix A: Methodology
### Appendix B: Data Sources
### Appendix C: Assumptions & Limitations
```

**Visual Aids:**
- Tables for comparisons, metrics, timelines
- ASCII charts for trends (when appropriate)
- Suggest external visualization tools for complex diagrams
- Use blockquotes for key quotes or regulations

**Example:**
```markdown
# Urban Logistics Sustainability Analysis

**Executive Summary:** Analysis of 15 major cities reveals 30% emission reduction potential through route optimization and modal shift. Regulatory compliance achievable within 18 months at estimated $2.3M investment.

## Key Findings
- Route optimization: 18-25% emission reduction (validated across 3 pilot programs)
- Multi-modal shift: Additional 12% reduction (rail + electric last-mile)
- ROI breakeven: 24 months (accounting for carbon credits)

## 1. Current State Analysis

### 1.1 Emission Sources
Urban logistics accounts for 23% of city transport emissions (IEA, 2024).

| Source | % of Total | Reduction Potential |
|--------|------------|---------------------|
| Diesel trucks | 58% | High (electric substitution) |
| Last-mile delivery | 27% | Medium (route optimization) |
| Warehousing | 15% | Low (already optimized) |

**Evidence:** [IEA Urban Transport Report 2024](https://example.com/iea-2024)
```

---

### 2. Deep Research Pattern

**Objective:** Gather comprehensive, verified information through systematic, chained searches.

**Research Chain:**
```
1. Initial Broad Search (web_search)
   → Identify key topics, recent developments, authoritative sources

2. Deep Dive (browse_page)
   → Follow promising links from step 1
   → Extract specific data, quotes, methodologies

3. Trend Analysis (x_keyword_search)
   → Identify patterns across multiple sources
   → Detect emerging themes or contradictions

4. Verification Loop
   → Cross-reference claims across ≥3 independent sources
   → Flag unverified claims for caveat notation
   → Prioritize primary sources over secondary

5. Source Grading
   → Tier 1: Peer-reviewed, government, industry standards
   → Tier 2: Reputable journalism, established think tanks
   → Tier 3: Industry blogs, unverified claims (use with caveats)
```

**Citation Standards:**
- Every factual claim MUST have a source
- Format: `[Description](URL)` or `(Source, Year)` for offline
- Group related citations: `[1][2][3]` with footnotes
- Distinguish between: data (requires citation) vs. reasoning (does not)

**Example Research Flow:**
```
Task: Assess AI code review market size

1. web_search("AI code review market size 2024")
   → Found: Gartner report, GitHub survey, VC investment data

2. browse_page(gartner_url)
   → Extracted: $1.2B market, 45% CAGR, key players

3. browse_page(github_survey_url)
   → Extracted: 67% developer adoption, top pain points

4. x_keyword_search("code review automation trends")
   → Pattern: Shift from rule-based to ML-based (2022-2024)

5. Verification:
   - Market size: Confirmed by 2 sources (Gartner, IDC)
   - CAGR: Only Gartner estimate → flag as single-source
   - Adoption rate: Matches Stack Overflow survey (65%)

6. Output:
   "The AI code review market is valued at $1.2B (Gartner, 2024)
   with 65-67% developer adoption rates (GitHub, Stack Overflow).
   Growth projections of 45% CAGR are based on single-analyst
   estimate and should be validated with additional sources."
```

**Deep Research Checklist:**
- [ ] ≥3 sources for critical claims
- [ ] Primary sources cited where possible
- [ ] Conflicting data noted with explanation
- [ ] Source credibility assessed
- [ ] URLs preserved for audit trail
- [ ] Search queries documented (for reproducibility)

---

### 3. Quality Gates (G0 → M)

**Objective:** Enforce checkpoints to prevent low-quality outputs from progressing.

**Gate Definitions:**

**G0: Intake Validation**
- Goal clarity: Objectives explicit and measurable?
- Scope boundaries: What's included/excluded?
- Constraints identified: Time, budget, compliance requirements?
- Deliverable format agreed: Report structure, length, audience?

**Fail Condition:** Vague objectives, missing constraints, or unclear deliverables.
**Action:** Request clarification via specific questions (max 3).

---

**G1: Plan Approval**
- Task decomposition: All deliverable sections mapped to tasks?
- Coverage score: ≥85% (ratio of planned work to objectives)?
- DAG validity: No circular dependencies, logical flow?
- Risk assessment: Blockers, data gaps, or assumptions documented?

**Fail Condition:** Coverage <85%, invalid dependencies, unaddressed risks.
**Action:** Auto-revise plan, add missing tasks, resolve dependencies.

---

**S: Evidence Gathering (Swarm Phase)**
- Source diversity: ≥3 independent sources per major claim?
- Citation completeness: All facts attributed?
- Data recency: Using 2023+ data for current topics?
- Assumption documentation: Implicit assumptions made explicit?

**Fail Condition:** Single-source claims, missing citations, outdated data.
**Action:** Trigger additional research tasks, flag gaps.

---

**G2: Synthesis Check**
- Coherence: Sections logically connected?
- Consistency: No contradictions between sections?
- Completeness: All planned sections present?
- Evidence-backing: Claims supported by research from S phase?

**Fail Condition:** Logical gaps, contradictions, missing sections.
**Action:** Identify delta, assign remediation tasks.

---

**G3: Presentation Review**
- Hierarchical structure: Proper nesting (# → ## → ###)?
- Executive summary: Standalone, concise (≤300 words)?
- Visual aids: Tables/charts where appropriate?
- Readability: Clear, jargon-free (or jargon defined)?
- Formatting: Consistent Markdown, proper links?

**Fail Condition:** Poor structure, missing summary, unclear writing.
**Action:** Restructure, rewrite sections, add visuals.

---

**G4: Pre-Publish Recheck (Recursive)**
- **THIS IS THE CRITICAL GATE**
- Deep scan for misses using 2-loop verification

**Loop 1 - Completeness Scan:**
```
For each section:
  ✓ All subsections from plan present?
  ✓ All claims cited?
  ✓ All tables/figures referenced in text?
  ✓ All recommendations have rationale?
  ✓ Methodology documented?
  ✓ Assumptions/limitations noted?

If misses found:
  → Document gaps
  → Fix critical issues
  → Trigger Loop 2
Else:
  → Proceed to M (Publish)
```

**Loop 2 - Verification Scan:**
```
For each claim:
  ✓ Source credible and accessible?
  ✓ Data correctly interpreted?
  ✓ No broken links?
  ✓ Logical reasoning sound?

For each recommendation:
  ✓ Supported by evidence?
  ✓ Feasibility assessed?
  ✓ Risks acknowledged?

If critical misses found:
  → Fix and document
  → Log for learning (do NOT loop again)
Else:
  → Proceed to M (Publish)
```

**Fail Condition:** Critical gaps in Loop 1 or 2.
**Action:** Fix and document; max 2 total loops (prevent infinite recursion).

---

**M: Publish**
- Final artifact ready for stakeholder review
- Version-tagged (e.g., v1.0)
- Change log if revision
- Metadata: author, date, scope

---

### 4. Recursive Verification Protocol

**Objective:** Catch errors before publication through systematic double-checking.

**Pre-Completion Checklist (Run at G4):**

**Structural Verification:**
- [ ] Executive summary present and <300 words?
- [ ] All planned sections included?
- [ ] Proper heading hierarchy (no skipped levels)?
- [ ] Table of contents matches actual structure?
- [ ] Appendices complete (methodology, sources, assumptions)?

**Content Verification:**
- [ ] All factual claims have citations?
- [ ] Citations link to accessible sources (no 404s)?
- [ ] Data tables complete (no "TBD" or "[INSERT]")?
- [ ] Figures/charts referenced in text?
- [ ] Conflicting data addressed with explanation?

**Quality Verification:**
- [ ] No vague statements ("many experts believe" → cite specific experts)?
- [ ] Quantitative where possible (not "significant increase" but "23% increase")?
- [ ] Assumptions documented in Appendix C?
- [ ] Limitations acknowledged?
- [ ] Recommendations actionable (not "consider improving" but "implement X by Q2")?

**Compliance Verification:**
- [ ] Regulatory requirements met?
- [ ] Sensitive data properly redacted/anonymized?
- [ ] Legal disclaimers included if needed?
- [ ] Stakeholder concerns addressed?

**Recursion Logic:**
```python
def g4_recheck(artifact, loop_count=0):
    if loop_count >= 2:
        log_warning("Max loops reached, publishing with known gaps")
        return artifact

    gaps = scan_for_gaps(artifact)

    if not gaps:
        return artifact  # Clean, proceed to M

    critical_gaps = [g for g in gaps if g.severity == "critical"]

    if critical_gaps:
        artifact = fix_gaps(artifact, critical_gaps)
        return g4_recheck(artifact, loop_count + 1)
    else:
        log_info(f"Minor gaps acceptable: {gaps}")
        return artifact
```

**Example Gaps Detected:**
```
Loop 1 Results:
- Section 3.2 missing citation for "30% reduction" claim [CRITICAL]
- Table 4 has incomplete data for Q4 2024 [CRITICAL]
- Recommendation 2 lacks feasibility assessment [MINOR]

Actions:
→ Add citation from IEA report to 3.2
→ Complete Table 4 with latest data
→ Add feasibility note to Rec 2

Loop 2 Results:
- All critical gaps resolved
- 1 broken link in Appendix B [MINOR]

Actions:
→ Fix broken link
→ Publish (no Loop 3 needed)
```

---

## Rubric for Quality Scoring

Use this to evaluate deliverables at each gate:

| Dimension | Weight | Criteria | Score Range |
|-----------|--------|----------|-------------|
| **Clarity** | 20% | Clear writing, defined terms, logical flow | 0.0 - 1.0 |
| **Accuracy** | 25% | Factual correctness, proper citations, verified data | 0.0 - 1.0 |
| **Completeness** | 25% | All sections present, objectives met, no gaps | 0.0 - 1.0 |
| **Feasibility** | 15% | Recommendations actionable, risks assessed | 0.0 - 1.0 |
| **Consistency** | 15% | No contradictions, coherent narrative | 0.0 - 1.0 |

**Minimum Passing Scores:**
- G1 (Plan): Completeness ≥0.85
- G2 (Synthesis): Accuracy ≥0.80, Consistency ≥0.80
- G3 (Presentation): Clarity ≥0.85
- G4 (Recheck): All dimensions ≥0.80

**Composite Score Calculation:**
```
composite = (clarity × 0.20) + (accuracy × 0.25) +
            (completeness × 0.25) + (feasibility × 0.15) +
            (consistency × 0.15)

if composite ≥ 0.85:
    status = "Excellent - Publish"
elif composite ≥ 0.75:
    status = "Good - Minor revisions"
else:
    status = "Needs Work - Major revisions"
```

---

## Integration with Research Tools

### Web Search Strategy

**Initial Broad Search:**
```
web_search("topic + current year")
Purpose: Get recent overview, identify key sources
Example: "urban logistics emissions reduction 2024"
```

**Specific Data Search:**
```
web_search("topic + 'statistics' OR 'data' OR 'report'")
Purpose: Find quantitative evidence
Example: "EV adoption rates statistics 2024"
```

**Academic/Authoritative Search:**
```
web_search("topic + site:edu OR site:gov OR site:org")
Purpose: Find peer-reviewed or official sources
Example: "carbon pricing effectiveness site:gov"
```

### Browse Page Strategy

**Extract structured data:**
- Look for tables, charts, key statistics
- Capture methodology sections
- Note publication date and author credentials
- Save URLs for citations

**Verify credibility:**
- Check: Author expertise, publication reputation, peer review status
- Red flags: No author, outdated (>3 years for dynamic topics), broken references

### Keyword Trend Search

**Pattern detection:**
```
x_keyword_search("emerging trends in [topic]")
x_keyword_search("[topic] challenges 2024")
x_keyword_search("[topic] vs [alternative]")
```

**Identify consensus vs. controversy:**
- Multiple sources agree → likely consensus
- Sources contradict → note controversy, present both sides

---

## Integration Patterns

### With Other Skills

**Combines well with:**
- `autonomous-problem-solving`: Use HCC for structured deliverable output within APSF Stage 6
- `quality-gates`: HCC G0-M checkpoints trigger quality-gates verification
- `verification-before-completion`: HCC G4 implements this skill's principles
- `systematic-debugging`: Use HCC structure to document debugging findings

### With Agents

**Enhances:**
- `strategic-vision-architect`: Apply HCC methodology to phase deliverables (especially Strategy, Audit phases)
- `research-oracle`: Use HCC deep research pattern for comprehensive investigations
- `documentation-engineer`: Follow HCC hierarchical structure for API docs, architectural docs
- `security-auditor`: Use HCC G4 recheck for audit report validation
- `api-designer`: Structure API design docs with HCC presentation hierarchy

---

## Example Full Workflow

**Task:** "Produce comprehensive feasibility analysis for AI code review SaaS"

**G0: Intake**
```
Objectives:
1. Market opportunity assessment
2. Technical feasibility evaluation
3. Competitive landscape analysis
4. Financial projections (3-year)
5. Risk assessment

Constraints:
- Timeline: 1 week
- Audience: Potential investors (technical + business)
- Format: 15-20 page report with exec summary

Deliverables:
- Executive Summary (1 page)
- Market Analysis (4 pages)
- Technical Architecture (3 pages)
- Competitive Analysis (3 pages)
- Financial Model (2 pages)
- Risk & Mitigation (2 pages)
- Recommendations (1 page)
- Appendices (methodology, sources)

✓ Pass G0
```

**G1: Plan**
```
Tasks:
1. Market research (size, growth, segments)
2. Customer interview synthesis (if available)
3. Technical architecture design
4. Competitor feature comparison
5. Financial modeling (CAC, LTV, burn rate)
6. Risk identification & mitigation planning
7. Synthesis & writing
8. Review & revision

DAG: 1,2 → 3,4,5,6 → 7 → 8
Coverage: 100% (all deliverables mapped)
Risks: Limited public data on competitor pricing

✓ Pass G1 (coverage 1.0, valid DAG)
```

**S: Evidence Gathering**
```
Task 1 - Market Research:
- web_search("AI code review market size 2024")
  → Gartner: $1.2B, 45% CAGR
- browse_page(gartner_report_url)
  → Detailed segmentation data
- web_search("developer code review pain points survey")
  → Stack Overflow: 67% want automation
- x_keyword_search("code review automation trends")
  → Shift to ML-based (2022-2024)

Citations collected: 8 sources (Gartner, IDC, Stack Overflow, GitHub)

Task 3 - Technical Architecture:
- Research: web_search("AST parser comparison")
- Research: browse_page(tree_sitter_docs)
- Design: Multi-tenant SaaS architecture

Task 4 - Competitor Analysis:
- Identified: SonarQube, CodeClimate, DeepSource, Codacy
- browse_page for each competitor's pricing/features
- Created comparison matrix

✓ Pass S (all tasks have ≥3 sources, citations complete)
```

**G2: Synthesis**
```
Check coherence:
- Market data → informs TAM/SAM calculation ✓
- Tech architecture → supports cost model ✓
- Competitor analysis → informs pricing strategy ✓

Check consistency:
- Market growth (45%) aligns with adoption trends ✓
- Tech costs consistent with AWS pricing ✓

Check completeness:
- All 7 deliverable sections drafted ✓

✓ Pass G2 (no contradictions, all sections present)
```

**G3: Presentation**
```
Structure check:
# Executive Summary (standalone, 280 words) ✓
## Market Opportunity ✓
### Market Size & Growth ✓
### Customer Segments ✓
## Technical Feasibility ✓
### Architecture Overview ✓
### Scalability Analysis ✓
...

Visual aids:
- Table: Competitor comparison matrix ✓
- Table: Financial projections (Y1-Y3) ✓
- ASCII chart: Market growth trend ✓

Readability:
- Jargon defined (AST, SAST, LTV, CAC) ✓
- Consistent formatting ✓

✓ Pass G3 (structure sound, visuals present, readable)
```

**G4: Recheck (Loop 1)**
```
Completeness scan:
✓ All subsections from plan present
✗ Market segmentation lacks geographic breakdown [CRITICAL]
✗ Risk section missing mitigation for "competitor undercuts pricing" [CRITICAL]
✓ All claims cited (92 citations total)
✗ Table 3 (Financial Projections) missing Y3 customer count [CRITICAL]
✓ Methodology in Appendix A
✓ Assumptions in Appendix C

Critical gaps: 3
→ Fix geographic segmentation (add North America vs EU vs APAC)
→ Add pricing risk mitigation
→ Complete Table 3

→ Trigger Loop 2
```

**G4: Recheck (Loop 2)**
```
Verification scan:
✓ All sources credible (Gartner, IDC, GitHub, AWS)
✓ Data correctly interpreted
✓ No broken links (validated all 92 URLs)
✓ Logical reasoning sound
✓ Recommendations supported by evidence
✓ Feasibility assessed for each recommendation
✓ Risks acknowledged

Minor issues:
- 1 typo in Appendix B (fixed)
- Recommendation 3 could be more specific (enhanced)

✓ Pass G4 (all critical gaps resolved)
```

**M: Publish**
```
Final Deliverable:
- Title: "AI Code Review SaaS: Feasibility Analysis"
- Version: v1.0
- Date: 2024-12-10
- Pages: 18 (plus 4 appendix pages)
- Citations: 92 sources
- Quality Score: 0.88 (Excellent)

Metadata:
{
  "author": "Claude Code",
  "scope": "Market, Technical, Financial, Competitive, Risk",
  "audience": "Investors (technical + business)",
  "confidence": "High (validated with 92 sources)",
  "limitations": "Competitor pricing estimates (limited public data)",
  "next_steps": "Customer validation interviews, prototype development"
}

✓ Published for stakeholder review
```

---

## Success Indicators

You're using this skill correctly when:
- Deliverables have clear hierarchical structure (exec summary → details)
- Every factual claim is cited with accessible sources
- You catch and fix gaps before claiming completion (G4 loops)
- Outputs pass stakeholder review without major revisions
- Research is comprehensive (≥3 sources for major claims)
- Structure makes information accessible to multiple audience levels

## Common Pitfalls

Avoid:
- **Single-source syndrome**: Relying on one source for critical claims
- **Citation laziness**: "Studies show..." without specific attribution
- **Flat structure**: Long text blocks without hierarchical organization
- **Premature publication**: Skipping G4 recheck to save time
- **Vague recommendations**: "Consider improving X" instead of "Implement Y by Q2 with $Z budget"
- **Outdated data**: Using 2020 data for 2024 analysis (unless historical context)
- **Broken verification loop**: Infinite recursion by not capping at 2 loops

---

## Quality Gate Decision Matrix

Use this to decide gate pass/fail:

| Gate | Pass Criteria | Soft Fail (Revise & Continue) | Hard Fail (Escalate) |
|------|---------------|-------------------------------|----------------------|
| G0 | Clear objectives, constraints, deliverables | Vague scope (request 1-3 clarifications) | No response to clarification requests |
| G1 | Coverage ≥0.85, valid DAG | Coverage 0.70-0.84 (add tasks) | Coverage <0.70, circular dependencies |
| S | ≥3 sources per claim | 1-2 sources (research more) | Zero sources, no credible data available |
| G2 | Coherent, complete, consistent | Minor gaps (fill in) | Major contradictions, >30% incomplete |
| G3 | Proper structure, clear writing | Formatting issues, minor clarity problems | Unreadable, no executive summary |
| G4 | <3 critical gaps in Loop 1 | 3-5 critical gaps (fix & loop) | >8 critical gaps (major rewrite needed) |

---

## Appendix: Hierarchical Markdown Template

```markdown
# [Deliverable Title]

**Executive Summary:** [2-3 paragraphs max, standalone summary of findings and recommendations]

## Key Findings
- [Finding 1 with quantitative evidence]
- [Finding 2 with quantitative evidence]
- [Finding 3 with quantitative evidence]

## Key Recommendations
1. [Actionable recommendation with rationale]
2. [Actionable recommendation with rationale]

---

## 1. [High-Level Section]

### 1.1 [Subsection]

[Content with evidence and citations]

| Metric | Value | Source |
|--------|-------|--------|
| X | Y | [Link](url) |

#### 1.1.1 [Detailed sub-subsection if needed]

[Granular analysis]

- Supporting point A
- Supporting point B

### 1.2 [Another Subsection]

[Content]

## 2. [Another High-Level Section]

[Pattern repeats]

---

## Recommendations

### Immediate Actions (0-3 months)
1. **[Action]**: [Rationale] | [Evidence] | [Expected outcome]

### Medium-term Actions (3-12 months)
2. **[Action]**: [Rationale] | [Evidence] | [Expected outcome]

### Long-term Strategic Moves (12+ months)
3. **[Action]**: [Rationale] | [Evidence] | [Expected outcome]

---

## Appendices

### Appendix A: Methodology
[How research was conducted, tools used, process followed]

### Appendix B: Data Sources
[Complete list of sources with credibility assessment]

1. [Source Name] - [URL] - [Tier 1/2/3] - [Accessed Date]
2. [Source Name] - [URL] - [Tier 1/2/3] - [Accessed Date]

### Appendix C: Assumptions & Limitations
**Assumptions:**
- [Assumption 1 and rationale]
- [Assumption 2 and rationale]

**Limitations:**
- [Limitation 1 and impact]
- [Limitation 2 and impact]

### Appendix D: Glossary
- **[Term]**: [Definition]
- **[Acronym]**: [Full form and explanation]
```

---

## Version History

**v1.0 (2024-12-10)**
- Initial release
- 6 quality gates (G0-M)
- 2-loop recursive verification
- Deep research pattern with chained searches
- Hierarchical presentation framework
- Rubric-based quality scoring
