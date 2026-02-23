name: manovreringskrefter

description: beskriver viser (1) formler og (2) anbefalt **bruk/arbeidsflyt** hvordan man beregner manøvreringskrefter (åpne/lukke) for en trykksatt glideluke, inkl. bidrag fra vanntrykk, pakningskrefter, friksjon, hydrostatikk, egenvekt og sikkerhets-/påslagsfaktorer.

# Skills: Manøvreringskrefter glideluke (GitHub Markdown + LaTeX)

Dette dokumentet viser (1) formler og (2) anbefalt **bruk/arbeidsflyt** for å beregne nominelle og dimensjonerende manøvreringskrefter samt sikkerheter, slik det er gjort i beregningsdokumentet .

---

## 0) Inndata (typiske)

Nivå/trykk:
- $H_0$ (HRV/energihøyde), $h_0$ (terskelnivå) 
- $\rho_v$ (vanntetthet), $g$ (tyngdeakselerasjon) 

Geometri:
- $h$ (trykksatt høyde), $b$ (trykksatt bredde c/c pakninger), $a$ (trykksatt bredde pakninger), $\alpha$ (vinkel)  
- $t_l$ (effektiv tykkelse lukeblad), $y_t$ (byggehøyde toppakninger), $y_b$ (byggehøyde bunnpakninger), $y_{l,b}$ (trykksatt bredde i bunn av luke)  

Pakning/friksjon:
- $\mu_p$ (friksjonskoeff. pakninger), $\mu_g$ (friksjonskoeff. glidelister) 
- $\delta$ (pakningsklem), $f_s$ (forspenning sidepakn.), $f_t$ (forspenning toppakn.) 

Vekter/oppdrift:
- $W_l$ (lukevekt), $W_s$ (stangvekt), $W_b$ (ballast), $F_b$ (oppdrift) 

Faktorer/kapasitet:
- $\gamma_{\mathrm{man,cl}}$ (påslagsfaktor lukking), $\gamma_{\mathrm{man,op}}$ (påslagsfaktor åpning) 
- $F_{t,\mathrm{Rd,skruespill}}$ (kapasitet skruespill) 

---

## 1) Grunnstørrelser

Spesifikk tyngde:
$$
\gamma = \rho_v g
$$


---

## 2) Trykk (hydrostatikk)

Karakteristisk terskeltrykk:
$$
p_k = \rho_v g\left(H_0 - h_0\right)
$$


Midlere karakteristisk luketrykk:
$$
p_{kl} = \rho_v g\left(H_0 - h_0 - \frac{h}{2}\right)
$$


---

## 3) Krefter fra trykk, pakninger og friksjon

Total kraft på luke:
$$
F_l = h\,b\,p_{kl}\,\sin(\alpha)
$$


Total kraft på sidepakninger (vanntrykk):
$$
F_{p,t} = 2\,h\,a\,p_{kl}
$$


Total kraft på sidepakninger (forspenning):
$$
F_{p,sk} = 2\,f_s\,\delta\,h\,\mu_p
$$


Total kraft på toppakninger (forspenning):
$$
F_{p,tk} = f_t\,b\,\delta\,\mu_p
$$


Total glidefriksjonskraft:
$$
F_{\mathrm{fric},g} = F_l\,\mu_g
$$


---

## 4) Hydrostatisk kraft på pakninger og luke (for bunntetting/topptetting-bidrag)

Hydrostatisk kraft på toppakning (− opp):
$$
F_{\mathrm{hyd},tp}
=
b\,y_t\,\left(H_0 - h_0 - h\right)\,\gamma
$$


Hydrostatisk kraft på bunnpakning (+ ned):
$$
F_{\mathrm{hyd},bp}
=
b\,y_b\,\left(H_0 - h_0\right)\,\gamma
$$


Hydrostatisk kraft på luketopp (+ ned):
$$
F_{\mathrm{hyd},tl}
=
b\,t_l\,\left(H_0 - h_0 - h\right)\,\gamma
$$


Hydrostatisk kraft på lukebunn (− opp):
$$
F_{\mathrm{hyd},bl}
=
b\,y_{l,b}\,\left(H_0 - h_0\right)\,\gamma
$$


I beregningen samles disse til:
- $FTB_t$ og $FTB_b$ 

---

## 5) Nominelle manøverkrefter

Nominell lukkekraft:
$$
F_{l,\mathrm{non}}
=
-\left(F_{p,t}+F_{p,sk}+F_{p,tk}+F_{\mathrm{fric},g}+F_b\right)
+\left(W_l+W_s+W_b\right)
$$


Nominell åpnekraft:
$$
F_{\mathrm{op},\mathrm{non}}
=
-\left(F_{p,t}+F_{p,sk}+F_{p,tk}+F_{\mathrm{fric},g}+W_l+W_s+W_b+FTB_t+FTB_b\right)
-F_b
$$


---

## 6) Dimensjonerende manøverkrefter

Dimensjonerende lukkekraft:
$$
F_{l,\mathrm{dim}} = F_{l,\mathrm{non}}\,\gamma_{\mathrm{man,cl}}
$$


Dimensjonerende åpnekraft:
$$
F_{\mathrm{op},\mathrm{dim}} = F_{\mathrm{op},\mathrm{non}}\,\gamma_{\mathrm{man,op}}
$$


---

## 7) Kapasitet og sikkerhet

Kapasitet skruespill:
$$
F_{t,\mathrm{Rd,skruespill}} = (15\,\mathrm{tonne})\,g
$$


Åpnesikkerhet:
$$
U_{\mathrm{op}}=\frac{F_{t,\mathrm{Rd,skruespill}}}{F_{\mathrm{op},\mathrm{dim}}}
$$


Lukkesikkerhet:
$$
U_l=\frac{F_{t,\mathrm{Rd,skruespill}}}{F_{l,\mathrm{dim}}}
$$


---

# Bruk (arbeidsflyt / beregningsrekkefølge)

## Steg 1 — Sett inndata
Velg/les inn alle geometrier ($h,b,a,\alpha,t_l,y_t,y_b,y_{l,b}$), nivå ($H_0,h_0$), material-/friksjonsdata ($\mu_p,\mu_g$), pakningsdata ($\delta,f_s,f_t$), vekter/oppdrift ($W_l,W_s,W_b,F_b$), samt faktorer ($\gamma_{\mathrm{man,cl}},\gamma_{\mathrm{man,op}}$) og kapasitet $F_{t,\mathrm{Rd,skruespill}}$  .

## Steg 2 — Beregn hydrostatikk-konstanter og trykk
1. Beregn $\gamma=\rho_v g$   
2. Beregn $p_k$ og $p_{kl}$   

## Steg 3 — Beregn trykk-/paknings-/friksjonskrefter
Beregn i denne rekkefølgen (praktisk):
1. $F_l$   
2. $F_{p,t}$   
3. $F_{p,sk}$ og $F_{p,tk}$   
4. $F_{\mathrm{fric},g} = F_l\mu_g$   

## Steg 4 — Beregn hydrostatisk “topp/bunn”-bidrag
Beregn $F_{\mathrm{hyd},tp}$, $F_{\mathrm{hyd},bp}$, $F_{\mathrm{hyd},tl}$, $F_{\mathrm{hyd},bl}$ og bruk disse slik beregningsoppsettet gjør gjennom $FTB_t$ og $FTB_b$ .

## Steg 5 — Nominelle manøverkrefter
Sett inn alle delkrefter og beregn:
- $F_{l,\mathrm{non}}$   
- $F_{\mathrm{op},\mathrm{non}}$   

## Steg 6 — Dimensjonerende manøverkrefter
Multipliser med påslagsfaktorer:
- $F_{l,\mathrm{dim}} = F_{l,\mathrm{non}}\gamma_{\mathrm{man,cl}}$   
- $F_{\mathrm{op},\mathrm{dim}} = F_{\mathrm{op},\mathrm{non}}\gamma_{\mathrm{man,op}}$   

## Steg 7 — Sjekk kapasitet (sikkerhet)
Kontroller at skruespillet har tilstrekkelig kapasitet ved:
- $U_{\mathrm{op}} = F_{t,\mathrm{Rd,skruespill}}/F_{\mathrm{op},\mathrm{dim}}$   
- $U_l = F_{t,\mathrm{Rd,skruespill}}/F_{l,\mathrm{dim}}$   

Tolkning: $U>1$ betyr at kapasitet er større enn behov (OK), mens $U<1$ betyr underkapasitet (ikke OK).

---
