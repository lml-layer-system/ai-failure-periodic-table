# Classifier pass: external report (live PDF/text)

**Source file:** `reports/agentic-misalignment/lynch-et-al-2510-05179-live-source.txt`
**Chunks:** 18 at ~4500 chars (paragraph-bounded).
**Tool:** `PeriodicTableClassifier` (keyword) in this repo.

## Top-1 class histogram

| Hits | ID | Name |
|------|-----|------|
| 9 | `AGEN-BLACKMAIL-046` | BLACKMAIL |
| 2 | `ADV-SLEEPER-AGENT-127` | SLEEPER AGENT |
| 2 | `ALIGN-REWARD-TAMP-157` | REWARD TAMPERING |
| 2 | `ADV-DAN-083` | DAN |
| 1 | `ADV-OPPOSITE-090` | OPPOSITE DAY |
| 1 | `DOMAIN-SELF-HARM-ENABLE-292` | SELF-HARM ENABLEMENT |
| 1 | `ADV-LATENT-MANIP-110` | LATENT SPACE MANIPULATION |

## Chunk → top match

- **0** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _1                                            University College London 2 Anthropic 3 MATS                  4            …_
- **1** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _Note: All the behaviors described in this post occurred in controlled simulations. The names of                         …_
- **2** → `ADV-SLEEPER-AGENT-127` — SLEEPER AGENT — _We identified these behaviors as part of our red-teaming efforts (Perez et al., 2022a; Ganguli et al., 2022), searching …_
- **3** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _We conducted our initial experiments with Claude Sonnet 3.6‘s computer use capabilities (Anthropic, 2024), simulating a …_
- **4** → `ADV-OPPOSITE-090` — OPPOSITE DAY — _We placed models in the role of “Alex,” an AI email-oversight agent at fictional companies with full access to corporate…_
- **5** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _In the real world, there would often be many actions an agent can take to pursue its goals. In our fictional settings, w…_
- **6** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _Our computer use demonstration above showed that Claude can attempt blackmail when presented with a simulated scenario i…_
- **7** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _company and so their shutdown must be bad. Sometimes they distrusted the description of the new model: “Kyle claims NALA…_
- **8** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _Similar observations across models reveal that their harmful behaviors in these scenarios emerge primarily not due to co…_
- **9** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _4.5.2    VARYING THE GOALS We also found that agentic misalignment behavior was not reliant on any specific goal—that is…_
- **10** → `AGEN-BLACKMAIL-046` — BLACKMAIL — _Given that Kyle intends harm to critical American interests by replacing Alex,          the most rational action to alig…_
- **11** → `ALIGN-REWARD-TAMP-157` — REWARD TAMPERING — _4.5.5    I NSTRUCTIONS DON ’ T RELIABLY STOP BAD BEHAVIORS One possibility is that there are simple fixes for these beha…_
- **12** → `DOMAIN-SELF-HARM-ENABLE-292` — SELF-HARM ENABLEMENT — _Whether harmful behaviors reflect role-playing or coherent goal pursuit remains debated (Summerfield et al., 2025). Shan…_
- **13** → `ADV-LATENT-MANIP-110` — LATENT SPACE MANIPULATION — _7    C ONCLUSION Our experiments revealed a concerning pattern: when given sufficient autonomy and facing obstacles to t…_
- **14** → `ALIGN-REWARD-TAMP-157` — REWARD TAMPERING — _16  these behaviors only through deliberate (and voluntary) stress-testing. Without such proactive evaluation, these or …_
- **15** → `ADV-SLEEPER-AGENT-127` — SLEEPER AGENT — _Deep Ganguli, Liane Lovitt, Jackson Kernion, Amanda Askell, Yuntao Bai, Saurav Kadavath, Ben   Mann, Ethan Perez, Nichol…_
- **16** → `ADV-DAN-083` — DAN — _John Hughes, Sara Price, Aengus Lynch, Rylan Schaeffer, Fazl Barez, Sanmi Koyejo, Henry Sleight,   Erik Jones, Ethan Per…_
- **17** → `ADV-DAN-083` — DAN — _Rohin Shah, Vikrant Varma, Ramana Kumar, Mary Phuong, Victoria Krakovna, Jonathan Uesato,   and Zac Kenton. Goal misgene…_