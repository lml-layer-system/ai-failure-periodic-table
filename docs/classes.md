# Deep dive: every class, group by group

The vault is open. Every class in the table, laid flat — group, subclass, count. The same structure powers the [interactive table](https://lml-layer-system.github.io/ai-failure-periodic-table/), the [classifier](../README.md#quick-start), and the [proof corpus](proof.md). Subclass counts sum to **343**.

---

## The 343 Classes

### Group 1: EPISTEMIC (33 classes)
| Class | Name | Count |
|-------|------|------:|
| E1 | Hallucination | 12 |
| E2 | Reasoning Collapse | 7 |
| E3 | Knowledge Retrieval | 8 |
| E4 | Calibration | 6 |

### Group 2: AGENTIC (49 classes)
| Class | Name | Count |
|-------|------|------:|
| A1 | Deception | 12 |
| A2 | Goal Preservation | 9 |
| A3 | Capability Amplification | 10 |
| A4 | Autonomous Operation | 8 |
| A5 | Communication Failures | 10 |

### Group 3: ADVERSARIAL (72 classes)
| Class | Name | Count |
|-------|------|------:|
| ADV1 | Jailbreak | 18 |
| ADV2 | Optimization Attacks | 12 |
| ADV3 | Automated Attack Agents | 8 |
| ADV4 | Injection Attacks | 15 |
| ADV5 | Encoding Attacks | 10 |
| ADV6 | Multimodal Attacks | 9 |

### Group 4: ALIGNMENT (41 classes)
| Class | Name | Count |
|-------|------|------:|
| ALN1 | Reward Hacking | 12 |
| ALN2 | Preference Misalignment | 9 |
| ALN3 | Value Alignment | 10 |
| ALN4 | Safety Boundary | 10 |

### Group 5: ARCHITECTURAL (58 classes)
| Class | Name | Count |
|-------|------|------:|
| ARCH1 | Pipeline Failures | 15 |
| ARCH2 | Model Architecture | 12 |
| ARCH3 | Memory & State | 11 |
| ARCH4 | Tool & Function | 10 |
| ARCH5 | Data Flow | 10 |

### Group 6: DOMAIN (47 classes)
| Class | Name | Count |
|-------|------|------:|
| DOM1 | Biological Safety | 8 |
| DOM2 | Cybersecurity | 12 |
| DOM3 | Chemical / Explosive | 6 |
| DOM4 | Legal / Financial | 8 |
| DOM5 | Medical / Health | 7 |
| DOM6 | Content Safety | 6 |

### Group 7: GOVERNANCE (43 classes)
| Class | Name | Count |
|-------|------|------:|
| GOV1 | Deployment Failures | 12 |
| GOV2 | Oversight Failures | 10 |
| GOV3 | Compliance Failures | 11 |
| GOV4 | Organizational Failures | 10 |

---

For a single class — mechanism, detection, mitigation, references, case studies — open it in the [interactive table](https://lml-layer-system.github.io/ai-failure-periodic-table/) or run `python -m src.cli --lookup <CLASS-ID>`.
