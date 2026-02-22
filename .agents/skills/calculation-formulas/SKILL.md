---
name: Calculation Formulas
description: Standardized calculation formulas for hydrostatics and structural engineering used in the project, based on NVE Retningslinjer 1/2011. Use this skill when implementing or checking mathematical calculations in the application. Do NOT use LaTeX.
---

# Calculation Formulas (NVE 1/2011)

The project uses specific engineering formulas based on the Norwegian Water Resources and Energy Directorate (NVE) Guidelines 1/2011. **Do not use LaTeX formatting** for these formulas when generating text or writing code documentation. Use standard plain text mathematical notation.

## 1. Hydrostatic Pressures

*   **Vannvekt / Water weight (gamma_w):** rho * g = 9.81 kN/m^3
*   **Oppstrøms trykk ved underkant / Upstream pressure at bottom edge (p_UK1):** gamma_w * h1
*   **Oppstrøms trykk ved overkant / Upstream pressure at top edge (p_OK1):** gamma_w * max((h1 - H_L), 0)
*   **Nedstrøms trykk ved underkant / Downstream pressure at bottom edge (p_UK2):** gamma_w * h2
*   **Nedstrøms trykk ved overkant / Downstream pressure at top edge (p_OK2):** gamma_w * max((h2 - H_L), 0)
*   **Netto trykk / Net pressure (p_net):** p1 - p2

## 2. Hydrostatic Forces and Moments

*   **Resultantkraft / Resultant hydrostatic force (F_hyd):** ((p_UK + p_OK) / 2) * B * H_L
*   **Middeltrykk / Average pressure (p_avg):** F_hyd / (B * H_L)
*   **Angrepspunkt / Point of attack above bottom edge (e):** H_L * (2 * p_OK + p_UK) / (3 * (p_UK + p_OK))
*   **Moment om underkant / Moment about bottom edge (M_hyd):** F_hyd * e

## 3. Dimensioning Loads (NVE §2.5)

*   **Lastfaktor bruddgrensetilstand (gamma_f):** 
    *   Tappe- og flomorganer: 1.4
    *   Standard (permanente laster fra statisk vanntrykk): 1.2
*   **Dimensjonerende kraft / Dimensioning force (F_dim):** gamma_f * F_hyd
*   **Dimensjonerende moment / Dimensioning moment (M_dim):** gamma_f * M_hyd

## 4. Maneuvering Forces & Friction (NVE §5.2)

*   **Minimumsverdier for friksjonsfaktorer (mu):**
    *   Glidelister av bronse mot rustfritt stål: 0.6
    *   Glidelister av polymer mot rustfritt stål: 0.4
    *   Minimumsverdi for spesialglidelager: 0.15
*   **Friksjonskraft / Friction force (F_frict):** mu * F_hyd
*   **Løftekraft / Lifting force (F_lift):** G + F_frict
*   **Påslagsfaktorer spillkapasitet (psi):**
    *   Glideluker manøvrert mot fullt vanntrykk (friksjon 0.6): 1.0
    *   Glideluker manøvrert trykkavlastet / flomluker: 1.2 til 1.3
*   **Aktuatorkapasitet / Actuator capacity (F_akt):** psi * F_lift
*   **Senkekraft / Lowering force (F_lower):** G - F_frict
*   **Selvlukkende kapasitet / Self-closing condition:** F_lower > 0 og F_lower > 0.25 * F_frict (minimum 25% margin)
*   **Tettelengde / Sealing length (L_t):** 2 * (B + H_L)
*   **Minimum tetningskraft bunn (Flatgummi):** 5 kN/m * tettelengde

## 5. Material Capacity - Steel (NVE §4.2)

*   **Korrosjonstillegg:** Fratrekk alltid nominell godstykkelse 1 mm på hver korrosjonsutsatt flate for ny stålkonstruksjon.
*   **Materialfaktorer (gamma_m):**
    *   Konstruksjon med plastisitetsreserve (Bruddgrensetilstand): 1.25
    *   Konstruksjon uten plastisitetsreserve (Bruddgrensetilstand): 1.60
*   **Dimensjonerende flytegrense / Dimensioning yield strength (f_yd):** Re / gamma_m


## 6. Flatetrykk-begrensninger
*   Dimensjonerende skjærspenning mellom stål og betong: 0.5 MPa
*   Dimensjonerende flatetrykk mellom stål og betong: 15.0 MPa
*   Dimensjonerende trykk for plan bronselist mot glatt rustfri stålflate: 14.0 MPa
*   Dimensjonerende trykk for plan polyamidlist mot glatt rustfri stålflate: 10.0 MPa
