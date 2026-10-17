# Brakes, Not Benchmarks: Why Capable AI Needs a Control Layer at the Decision Boundary

**A position paper on decision control as infrastructure**

Author: Zhichen Ji
Affiliation: NOHN AI TECHNOLOGY PTE. LTD., Singapore
Contact: ai@nohnlins.com · ORCID 0009-0006-9578-5657
Date: 2026-10-17 · Version 1.0

---

## Abstract

Every system that moves something valuable has two independent mechanisms: one that converts energy into motion, and one that converts intention into stopping. For AI we have spent a decade industrialising the first and have largely assumed the second. This paper argues a category claim: the more capable an AI system becomes, the more it needs a **brake** — a control layer at the decision boundary that can deterministically hold or block a specific action before it becomes irreversible, on the basis of declared structure rather than predicted quality. A brake is not alignment training, not output filtering, not a benchmark, not an explanation, and not a process kill switch. It is an external, deterministic, non-advisory, offline-verifiable mechanism that stops the *action*, not the *process*, and leaves a sealed record of what was permitted and why. We give five reasons the layer is necessary, seven design requirements it must satisfy, five things it must never do, and responses to five standard objections. The argument is about a category, not a product: it makes no benchmark or comparative-performance claim.

**摘要** —— 任何承载价值的运动系统都有两套彼此独立的机构：一套把能量转成运动，一套把意图转成停止。AI 的前十年几乎全部投在后者之外的第一个问题上，第二个问题则被默认"会有办法"。本文论证一个类别主张：AI 能力越强，越需要一个**刹车系统**——位于决策边界、能在动作不可逆之前确定性地阻断或放行的控制层，其判据是"结构是否声明"，而不是"质量是否够高"。刹车不是对齐训练、不是输出过滤、不是基准测试、不是可解释性、也不是进程级急停。它是外部的、确定性的、非建议性的、可离线重算的机构：停的是**动作**，不是**进程**，并留下"什么被放行、为什么"的封存记录。本文给出五条必要性论证、七条设计要件、五条禁止项，并回应五种常见反对意见。全文讨论的是一个类别，不涉及任何基准或对比性能主张。

---

## 1. The Missing Component

A car is not defined by its engine. It is defined by the fact that the engine and the brakes were designed together, by different teams, under the same safety case. Remove the brakes and the engine does not become more powerful; it becomes unusable, because no one can permit it to move.

AI has been built the other way around. Capability is measured, published, compared, and funded. The ability to stop a specific action at a specific moment is assumed to follow from capability itself — from better training, better alignment, better evaluation, better model cards. It does not follow. It is a different component, with different properties, built by a different party, verified by a different method.

This paper states the case for that component.

**The claim.** A deployed AI system in any domain where actions have consequences needs a brake: a control layer at the decision boundary that can deterministically hold or block an action before it becomes irreversible, on the basis of declared structure rather than predicted quality.

**What this paper is not.** It is not a product description, a benchmark, or a certification claim. It argues for a category. Whether any particular implementation satisfies the argument is a separate, checkable question, and it should be checked rather than believed.

---

## 2. What Counts as a Brake

The word "safety" is used for too many different mechanisms. They act in different places, on different objects, with different failure modes. A brake is one specific thing.

| Mechanism | Where it acts | Can it stop a specific action? | Independent of the generator? | Deterministic? |
|---|---|---|---|---|
| Alignment training (RLHF, constitutional methods) | Model behaviour, in distribution | No — it shifts a distribution | No | No |
| Output filtering / guardrails | Generated text | Partially — pattern-based, post hoc | Partially | Usually |
| Benchmarks and evaluation suites | Before deployment | No — they inform a decision, they do not make one | Yes | Yes, but offline |
| Explainability methods | After an output exists | No | Partially | Varies |
| Process kill switch | Runtime process | Yes — by killing everything | Yes | Yes |
| **Decision brake** | **Decision boundary, upstream of actuation** | **Yes — the specific action** | **Yes** | **Yes** |

The critical distinction is the last two rows. A kill switch stops the process; a brake stops the action. Killing a process is a coarse, expensive, all-or-nothing intervention that is only acceptable after something has already gone wrong. A brake operates per decision, before actuation, and is therefore usable continuously — which is the only way a control can be relied on rather than reserved for emergencies.

Five properties follow from the definition. A brake must be:

1. **External** — it does not share the generator's weights, failure modes, or commercial incentives.
2. **Deterministic** — the same declared input, clock and nonce yield the same verdict, on any machine.
3. **Binding** — it acts on the decision-execution step, upstream of actuation, not on a dashboard after the fact.
4. **Bounded** — it blocks only on declared structural absence, never on a judgement about whether the decision is wise.
5. **Accountable** — it terminates in a named decision unit, not in "the system".

A mechanism missing any of these is a monitoring tool, a filter, or a promise. None of those is a brake.

---

## 3. Five Reasons the Layer Is Necessary

### 3.1 Capability is monotone; permission is not

Capability grows with scale, data, and compute. The set of actions a system can take grows with capability. Permission does not grow with it. Permission is granted explicitly, bounded explicitly, and must be revocable.

When permission is not represented by an independent mechanism, it is inferred from behaviour — which is to say, it defaults to whatever the system will do. That is not a permission model. It is an absence of one.

### 3.2 A stochastic system cannot promise

A promise is a statement about future behaviour. A sampled generator produces a distribution over behaviour. These are not the same object, and no amount of training converts one into the other.

"The model is aligned" is a claim about a tendency. "This action may proceed" is a decision about an instance. Governance obligations attach to instances: this decision, this assumption set, this responsible party, this moment. A tendency cannot satisfy an obligation about an instance. A mechanism can.

### 3.3 Consequence asymmetry

Expected-value reasoning fails when one branch is irreversible. A system that is right a thousand times and catastrophic once is not a good system with a bad tail; it is a system whose tail dominates its value.

The expensive failure in AI deployment is not a wrong sentence. It is an action taken on an assumption nobody declared, with no prepared response for the case where that assumption fails. Stopping distance is the budget a system reserves for being wrong. A system without that budget is not fast; it is uninsured.

### 3.4 Delegation without a stop is abdication

To delegate is to retain the right to stop. A delegation in which the delegator cannot halt the delegate is not delegation; it is transfer of control with retention of blame.

This is why a brake must terminate in a named decision unit — organisation, role, stage, owner — rather than in a model name or a vendor. Accountability that cannot be addressed cannot be exercised. A brake converts a diffuse "the system decided" into a specific "this unit permitted this action under these declared conditions".

### 3.5 Regulation is converging on control, not on outputs

The EU AI Act requires, for high-risk systems, a risk-management system (Article 9), technical documentation (Article 11, Annex IV), record-keeping (Article 12), transparency and instructions for use (Article 13), effective human oversight (Article 14), and accuracy, robustness and cybersecurity (Article 15). Deployers must retain automatically generated logs (Article 19), assign oversight to competent natural persons, and cooperate with authorities (Article 26); post-market monitoring is required (Article 72); third-party conformity assessment is the norm for many categories (Article 43). The GDPR grants data subjects the right to meaningful information about automated decision logic and to contest decisions (Article 22).

The NIST AI Risk Management Framework, ISO/IEC 42001, and Singapore's AI Verify framework differ in vocabulary but share a shape: they require **documented, demonstrable control exercised by an identifiable party at a defined point, with a retained record**.

None of these obligations is satisfied by a better model. They are satisfied by a control layer. A regulator does not ask whether the model was excellent; a regulator asks who could have stopped the action, on what basis, and what remains as proof that the stop was available.

---

## 4. Seven Design Requirements

**D1 — Independence.** The brake must not be owned, trained, or tuned by the party whose output it controls. Self-control is not control, for the same reason self-assessment is not assessment: the incentive structure is identical on both sides of the table.

**D2 — Determinism.** Identical declared input, clock, and nonce must yield an identical verdict and an identical record across machines. Reproducibility is what turns a control claim into something a third party can check rather than something a vendor can assert.

**D3 — Non-advisory by construction.** The brake must be structurally incapable of recommending, ranking, scoring, or optimising. If it can express advice, it becomes a second opinion generator, and neutrality is lost. The strongest form of this requirement is a construction guarantee: a decision language whose grammar cannot express a conclusion, a recommendation, a ranking, a score, or a probability. A tool that cannot advise cannot be recruited into advising.

**D4 — Asymmetric failure policy.** Structural absence may block; quantitative opinion may not. A missing assumption, a missing failure branch, a missing responsible unit — these block. A low probability, a poor score, an unfavourable comparison — these do not. This asymmetry is what prevents a brake from becoming a censor with a risk model attached.

**D5 — Binding at the decision boundary.** The brake sits downstream of generation and upstream of actuation. It stops the action, not the process. This is what makes it usable continuously: a kill switch is an emergency measure, a brake is an operating control.

**D6 — Offline verifiability.** A third party must be able to recompute the verdict and verify the record without the vendor, without the model, and without network access. Binding the record to a digest of the exact input — rather than to the input itself — keeps this compatible with data minimisation: the record proves which input was controlled without disclosing it.

**D7 — Versioned and frozen.** Grammar, verdict semantics, thresholds, and reference values carry version numbers and are frozen at release. A verdict must remain interpretable after the model that produced the decision has been retired, because the question "what did the system commit to" is asked years later.

---

## 5. What a Brake Must Never Do

1. **It must not decide what is true.** Truth is a separate axis. A claim can be factually correct and structurally opaque; it can be factually wrong and fully declared. A brake that adjudicates truth becomes an oracle, and an oracle cannot be verified.
2. **It must not rank or recommend.** Ranking is advice. Advice destroys neutrality and makes the control layer a party to the decision it is supposed to bound.
3. **It must not cap capability.** A brake is not a speed limit. It is the condition under which speed is permitted. Confusing the two produces safety theatre: systems that are slow, expensive, and no safer.
4. **It must not replace process safety.** Sandboxing, resource limits, and kill switches operate on the process. The brake operates on the decision. These are different layers with different failure modes, and neither substitutes for the other.
5. **It must not sell paperwork.** A control layer is not a certification mark. The deliverable is the ability to stop a specific action and to show that the ability existed. A certificate on a wall is not a brake.

---

## 6. The Economics of Stopping Distance

Brakes are usually argued as a cost. They are better understood as the thing that makes speed saleable.

**Insurance.** A risk becomes insurable when it is bounded and inspectable. "The model is good" is not inspectable. "This action was permitted because these assumptions were declared and these failure branches were prepared" is. A brake is what makes an AI risk legible enough to price, and therefore transferable.

**Procurement.** High-risk buyers do not need to be convinced that a model is excellent; they need to be able to defend a decision to their own board and regulator. "Trust us" and "check this" are different sales motions. The second one closes.

**Liability.** After an incident, the question is not what the model said. It is what the system committed to, on what assumptions, under whose signature. A sealed record answers that question. A transcript does not.

**Speed.** Organisations that can stop precisely are the ones permitted to move fast. The ones that cannot stop are slowed down by their own risk appetite, by insurers, and eventually by regulators. Braking capacity is throughput capacity.

---

## 7. Five Objections

**O1 — "This will slow AI down."**
Brakes do not reduce top speed; they define the envelope in which top speed is permitted. Without them, speed is capped not by technology but by tolerance for uninsured risk. The choice is not between fast and safe; it is between fast-with-brakes and slow-without.

**O2 — "Models will be good enough."**
Good enough is a property of a distribution, not of an instance. A distribution with a thin tail still has a tail, and the tail is where irreversible actions live. Brakes address the instance, which is the only place an action actually happens.

**O3 — "We already have alignment and guardrails."**
Alignment lives inside the engine and shares its failure modes. Guardrails filter text after it exists and are typically owned by the same party. Neither is independently verifiable by a third party, and neither can bind an action at the decision boundary. They are useful. They are not a brake.

**O4 — "This is just audit under a new name."**
No. Audit looks backward at records after the fact; its output is an opinion about what happened. A brake acts forward, at the moment of commitment, and its output is a decision about whether the action may proceed. The record is a by-product of control, not its purpose. An organisation that can only describe what happened has documentation; an organisation that can stop what is about to happen has control.

**O5 — "Who sets the thresholds?"**
The deployer, in advance, in a frozen standard. The brake enforces declared structure — did this decision declare the assumptions it depends on, and does it commit to a response when they fail — not the vendor's opinion about whether the decision is wise. Disagreement about thresholds is legitimate and belongs in the standard-setting process. Disagreement about whether a brake exists is not a matter of opinion.

---

## 8. Adoption Path

**Phase 1 — Deployer-side.** The first buyers are organisations with a duty of care over automated decisions: banks, insurers, hospitals, public agencies. They need one ruler across heterogeneous models, applied before the action, with a record they can defend. This phase requires no change to any model.

**Phase 2 — Vendor-integrated.** Once the category is established, brake layers ship as components rather than as promises. A vendor that can say "our output is bounded by an independently verifiable control" has a different liability posture from one that says "our model is safe".

**Phase 3 — Regulatory reference.** Control output becomes an input to conformity assessment and post-market monitoring: not a certificate, but evidence that a stop was available at the moment it was needed.

The precondition for all three is a public standard with deterministic semantics and published reference values, so that "the brake worked" is checkable rather than asserted. Standards precede markets; that is how every safety-critical industry got its brakes.

---

## 9. Conclusion

The question is not whether AI will be fast. It will be fast. The question is whether it can stop.

A system that cannot stop cannot be trusted with speed, no matter how capable it is. Capability without a stopping mechanism is not progress; it is uninsured exposure with a good demo. The brake is not the opposite of capability — it is the precondition of permission.

Build the engine. Then build the brake, separately, verifiably, and under someone else's signature.

---

## Status of This Document

This is a position paper. It argues for a category and makes no benchmark, comparative-performance, or certification claim. Implementation-level claims about any specific engine are outside its scope and must be checked against that engine's published specification and verifier.

---

## References

1. Regulation (EU) 2024/1689 of the European Parliament and of the Council (Artificial Intelligence Act), *Official Journal of the European Union*, 2024.
2. National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*, NIST AI 100-1, January 2023.
3. ISO/IEC 42001:2023, *Information technology — Artificial intelligence — Management system*.
4. AI Verify Foundation (Infocomm Media Development Authority, Singapore), *AI Verify: An AI Governance Testing Framework and Toolkit*.
5. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, J. Schulman, D. Mané, "Concrete Problems in AI Safety," arXiv:1606.06565, 2016.
6. S. Russell, *Human Compatible: Artificial Intelligence and the Problem of Control*, Viking, 2019.
7. N. G. Leveson, *Engineering a Safer World: Systems Thinking Applied to Safety*, MIT Press, 2011.
8. J. Reason, *Human Error*, Cambridge University Press, 1990.
9. Regulation (EU) 2016/679 (General Data Protection Regulation), Article 22, 2016.
10. R. C. Merkle, "A Digital Signature Based on a Conventional Encryption Function," *Advances in Cryptology — CRYPTO '87*, 1987.
