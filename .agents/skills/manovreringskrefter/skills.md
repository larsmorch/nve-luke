name: manovreringskrefter

description: Dette dokumentet beskriver hvordan man beregner manøvreringskrefter (åpne/lukke) for en trykksatt glideluke, inkl. bidrag fra vanntrykk, pakningskrefter, friksjon, hydrostatikk, egenvekt og sikkerhets-/påslagsfaktorer. Formlene under er hentet fra beregningsdokumentet  .


# Skills: Manøvreringskrefter glideluke (formler + bruk)


---

## 1) Konstanter og grunnstørrelser

### 1.1 Tyngdeakselerasjon og vanntetthet
- \( g \): tyngdeakselerasjon \([\mathrm{m/s^2}]\)
- \( \rho_v \): tetthet vann \([\mathrm{kg/m^3}]\) 

### 1.2 Spesifikk tyngde (hydrostatisk “gamma”)
\[
\gamma = \rho_v g
\]
Brukes for å konvertere vannsøylehøyde til trykk/last pr. areal. 

---

## 2) Trykk (hydrostatikk)

### 2.1 Karakteristisk terskeltrykk
\[
p_k = \rho_v g\left(H_0 - h_0\right)
\]
- \(H_0\): HRV/energihøyde (lokal høyde)
- \(h_0\): terskelnivå (lokal høyde) 

**Tolkning:** Trykket ved terskelnivå basert på vannstand over terskel.

### 2.2 Midlere karakteristisk luketrykk
\[
p_{kl} = \rho_v g\left(H_0 - h_0 - \frac{h}{2}\right)
\]
- \(h\): trykksatt høyde (relatert til pakning/geometri) 

**Tolkning:** Gjennomsnittstrykk over den trykksatte høyden (lineært trykkforløp).

---

## 3) Krefter fra vanntrykk og friksjon

### 3.1 Total kraft på luke (fra luketrykk)
\[
F_l = h\, b\, p_{kl}\,\sin(\alpha)
\]
- \(b\): trykksatt bredde/c-c pakninger
- \(\alpha\): lukebladets vinkel ift. horisontalplanet 

**Tolkning:** Resultant kraftkomponent som virker på luka (inkl. vinkel).

### 3.2 Total kraft på sidepakninger fra vanntrykk
\[
F_{p,t} = 2\, h\, a\, p_{kl}
\]
- \(a\): trykksatt bredde pakninger (målt i tegning) 

**Tolkning:** Vanntrykk som presser sidepakninger (to sider).

### 3.3 Forspenningskraft sidepakninger (gir friksjonsbidrag)
\[
F_{p,sk} = 2\, f_s\, \delta\, h\, \mu_p
\]
- \(f_s\): forspenningskraft/trykknivå sidepakninger
- \(\delta\): pakningsklem
- \(\mu_p\): friksjonskoeffisient pakninger 

**Tolkning:** Friksjonsrelatert kraftbidrag fra sidepakningers klem/forpenn.

### 3.4 Forspenningskraft toppakninger (gir friksjonsbidrag)
\[
F_{p,tk} = f_t\, b\, \delta\, \mu_p
\]
- \(f_t\): forspenningskraft/trykknivå toppakninger 

### 3.5 Total glidefriksjonskraft (glidelister)
\[
F_{\mathrm{fric},g} = F_l\, \mu_g
\]
- \(\mu_g\): friksjonskoeffisient glidelister 

---

## 4) Hydrostatisk opp-/neddrift på pakninger og luke

### 4.1 Kraft på toppakning (negativ = opp)
\[
F_{\mathrm{hyd},tp} = b\, y_t\,\left(H_0-h_0-h\right)\,\gamma
\]
- \(y_t\): byggehøyde toppakninger 

### 4.2 Kraft på bunnpakning (positiv = ned)
\[
F_{\mathrm{hyd},bp} = b\, y_b\,\left(H_0-h_0\right)\,\gamma
\]
- \(y_b\): byggehøyde bunnpakninger 

### 4.3 Kraft på luketopp (positiv = ned)
\[
F_{\mathrm{hyd},tl} = b\, t_l\,\left(H_0-h_0-h\right)\,\gamma
\]
- \(t_l\): effektiv tykkelse lukeblad 

### 4.4 Kraft på lukebunn (negativ = opp)
\[
F_{\mathrm{hyd},bl} = b\, y_{l,b}\,\left(H_0-h_0\right)\,\gamma
\]
- \(y_{l,b}\): trykksatt bredde i bunn av luke 

### 4.5 Bunntetting-bidrag (som brukt i dokumentet)
Dokumentet samler relaterte bidrag i:
- \(FTB_t\) og \(FTB_b\) (fra topp/bunn-relaterte hydrostatikkbidrag) 

---

## 5) Nominelle manøverkrefter (åpne/lukke)

### 5.1 Nominell lukkekraft
\[
F_{l,\mathrm{non}}
=
-\left(F_{p,t}+F_{p,sk}+F_{p,tk}+F_{\mathrm{fric},g}+F_b\right)
+\left(W_l+W_s+W_b\right)
\]
- \(W_l\): lukevekt
- \(W_s\): stangvekt
- \(W_b\): ballast
- \(F_b\): oppdrift  

**Tolkning:** Summerer motkrefter (pakninger/friksjon/oppdrift) og drivende krefter (egenvekter) med fortegn iht. dokumentets konvensjon.

### 5.2 Nominell åpnekraft
\[
F_{\mathrm{op},\mathrm{non}}
=
-\left(
F_{p,t}+F_{p,sk}+F_{p,tk}+F_{\mathrm{fric},g}
+W_l+W_s+W_b
+FTB_t+FTB_b
\right)
-F_b
\]


---

## 6) Dimensjonerende manøverkrefter (påslagsfaktorer)

### 6.1 Dimensjonerende lukkekraft
\[
F_{l,\mathrm{dim}} = F_{l,\mathrm{non}}\,\gamma_{\mathrm{man,cl}}
\]
- \(\gamma_{\mathrm{man,cl}}\): påslagsfaktor manøvrert lukking  

### 6.2 Dimensjonerende åpnekraft
\[
F_{\mathrm{op},\mathrm{dim}} = F_{\mathrm{op},\mathrm{non}}\,\gamma_{\mathrm{man,op}}
\]
- \(\gamma_{\mathrm{man,op}}\): påslagsfaktor manøvrert åpning  

---

## 7) Kapasitet og sikkerhet (skruespill)

### 7.1 Kapasitet skruespill
\[
F_{t,\mathrm{Rd,skruespill}} = (15~\mathrm{tonne})\, g
\]


### 7.2 Åpnesikkerhet
\[
U_{\mathrm{op}}=\frac{F_{t,\mathrm{Rd,skruespill}}}{F_{\mathrm{op},\mathrm{dim}}}
\]


### 7.3 Lukkesikkerhet
\[
U_l=\frac{F_{t,\mathrm{Rd,skruespill}}}{F_{l,\mathrm{dim}}}
\]


**Tolkning:** Forholdet mellom tilgjengelig kapasitet og nødvendig dimensjonerende kraft.

---

## 8) Inputliste (symboler fra dokumentet)

Geometri / nivå:
- \(H_0\), \(h_0\), \(h\), \(b\), \(a\), \(\alpha\), \(t_l\), \(y_t\), \(y_b\), \(y_{l,b}\)  

Material/friksjon/pakning:
- \(\mu_p\), \(\mu_g\), \(\delta\), \(f_s\), \(f_t\) 

Laster:
- \(W_l\), \(W_s\), \(W_b\), \(F_b\) 

Faktorer:
- \(\gamma_{\mathrm{man,op}}\), \(\gamma_{\mathrm{man,cl}}\) 

---

## 9) Bruk (beregningsrekkefølge)

1. Beregn \(\gamma=\rho_v g\)
2. Beregn \(p_k\) og \(p_{kl}\)
3. Beregn \(F_l\), \(F_{p,t}\), \(F_{p,sk}\), \(F_{p,tk}\), \(F_{\mathrm{fric},g}\)
4. Beregn hydrostatikkbidrag \(F_{\mathrm{hyd},*}\) og evt. bruk \(FTB_t, FTB_b\) iht. dokumentet
5. Beregn \(F_{l,\mathrm{non}}\) og \(F_{\mathrm{op},\mathrm{non}}\)
6. Multipliser med \(\gamma_{\mathrm{man,cl}}\) og \(\gamma_{\mathrm{man,op}}\) for dimensjonerende krefter

7. Kontroller \(U_{\mathrm{op}}\) og \(U_l\) mot kapasitet skruespill

Inline: $p=\rho g h$

$$
p_{kl}=\rho_v g\left(H_0-h_0-\frac{h}{2}\right)
$$

$p_{kl}=\rho_v g\left(H_0-h_0-\frac{h}{2}\right)$

