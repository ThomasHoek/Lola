4 | no
h: \B.exists a1.(exists a2.((exists a6.(-exists a7.(man(a7) & a6(a7)) & exists a5.(entity(a5) & a6(a5))) & exists a5.(-exists a6.((exists a8.exists a9.(exists a10.(buiten(a10) & a9(a10)) & exists b.persoon(b)(a9))(a8) & jongen(a8))(a6) & a5(a6)) & exists a4.(entity(a4) & a5(a4))))(exists b.persoon(b)))(a2) & a1(a2) & B(a1))
p: error
s: error
------------------------------
24 | unknown
h: (((\A B.A & B)(\B.(exists a4.één(a4) & wiel(B))))(((\A B.A & B)(\B.exists a5.(fiets(a5) & B(a5))))(\A.A(\a3.rijden(a3)))))(\B.exists a2.(exists a3.(persoon(a3) & a2(a3)) & B(a2)))
p: (((\A B.A & B)(\B.exists a4.(motor(a4) & B(a4))))(\B.exists a3.(exists a4.(truc(a4) & a3(a4)) & B(a3))))(\Q.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.zwart(a6) & jas(a5) & B(a5))))(\A B.(exists a3.A(exists b.persoon(b),a3) & B(a3))))(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
105 | unknown
h: error
p: sportschool(\C.in(\B.exists a3.(exists a4.(backbend(a4) & a3(a4)) & B(a3)),C),\Q.exists a2.(exists a3.vi(a3) & kind(a2) & Q(a2)))
s: error
------------------------------
116 | unknown
h: exists a2.(exists a3.(deel(a3) & exists a5.(voetbalwedstrijd(a5) & aan(a2,a5))) & exists z49.(exists a3.twee(a3) & team(z49) & a2(z49)))
p: exists a2.(bal(a2) & exists z47.(speler(z47) & a2(z47)))
s: (FATAL)
%%ERROR: The following symbols are used with multiple arities: aan/2, aan/1.


Fatal error:  The following symbols are used with multiple arities: aan/2, aan/1
------------------------------
119 | unknown
h: exists a2.(exists a4.(exists a5.houten(a5) & hut(a4) & in(a2,a4)) & exists z53.(exists a3.vijf(a3) & kind(z53) & a2(z53)))
p: exists a2.(exists a4.(exists a5.houten(a5) & hut(a4) & voor(a2,a4)) & exists z51.(exists a3.vijf(a3) & kind(z51) & a2(z51)))
s: (FATAL)
%%ERROR: The following symbols are used with multiple arities: in/2, in/1.


Fatal error:  The following symbols are used with multiple arities: in/2, in/1
------------------------------
185 | unknown
h: exists a4.(restaurant(a4) & in(\A.A(\a2.eten(a2)),a4))(\B.exists a2.(exists a3.groot(a3) & exists a4.(groep(a4) & aziaten(a2)) & B(a2)))
p: (((\A B.A & B)(\Q.exists a4.(verlichting(a4) & Q(a4))))(exists a5.(restaurant(a5) & in(\B.exists a4.(exists a6.(exists a7.rood(a7) & tafel(a6) & aan(a4,a6)) & B(a4)),a5))))(\Q.exists a2.(mens(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
197 | unknown
h: error
p: (\B.exists a4.(zadel(\C.op(a4,C)) & B(a4)) & \B.exists a3.(exists a5.(exists a6.zwartwit(a6) & motorfiets(a5) & op(a3,a5)) & B(a3)))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
s: error
------------------------------
211 | yes
h: (((\A B.A & B)(\B.exists a4.(plant(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\Q.exists a2.(exists a3.twee(a3) & hond(a2) & Q(a2)))
p: (((\A B.A & B)(\B.exists a4.(boom(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\Q.exists a2.(exists a3.twee(a3) & hond(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
218 | yes
h: (\A.A(\a3.dansen(a3)) & \B.exists a3.(exists a4.(exists a5.wit(a5) & kleren(a4) & a3(a4)) & B(a3)))(\B.exists a2.(meisje(a2) & B(a2)))
p: exists a2.((((\A B.A & B)(\a5.wit(a5)))(\a3.meisje(a3)))(a2) & dansen(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
219 | no
h: exists a2.((((\A B.A & B)(\a5.wit(a5)))(\a3.meisje(a3)))(a2) & dansen(a2))
p: error
s: error
------------------------------
225 | unknown
h: exists a2.((((\A B.A & B)(\a5.wit(a5)))(\a3.meisje(a3)))(a2) & dansen(a2))
p: (((\A B.A & B)(\B.(exists a6.blond(a6) & exists a7.(meisje(a7) & B(a7)))))(\a3.apparatuur(a3)))(\a2.solide(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
228 | unknown
h: exists a2.(geluidsapparatuur(\C.voor(a2,C)) & exists a3.blond(a3) & meisje(a2))
p: exists a2.((((\A B.A & B)(\a5.wit(a5)))(\a3.meisje(a3)))(a2) & dansen(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (geluidsapparatuur(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
236 | unknown
h: \B.exists a1.(((\Q.exists a7.(exists a8.drie(a8) & kind(a7) & Q(a7)) & \A B.exists a6.(A(a6) & B(a6)))(\C.aan(\B.exists a3.(exists a4.aziatisch(a4) & man(a3) & B(a3)),C)))(a1) & B(a1))
p: error
s: error
------------------------------
253 | yes
h: (\B F105.exists a6.(aan(B,a6) & F105(a6)) & \B.(top(\C.op(B,C)) & berg(\C.van(\C.op(B,C),C))))(\B.exists a2.(wandelaar(a2) & B(a2)))
p: (\B.exists a4.(exists a5.(exists a6.vreugdevol(a6) & dans(a5) & a4(a5)) & B(a4)) & \B.(top(\C.op(B,C)) & berg(\C.van(\C.op(B,C),C))))(\B.exists a2.(wandelaar(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B F105.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
280 | unknown
h: (((\A B.A & B)(\B.(exists a5.blauw(a5) & oceaan(B))))(\A.A(\a2.waden(a2))))(\a2.jongen(a2))
p: exists a2.(water(\C.buiten(a2,C)) & exists z123.(jongen(z123) & a2(z123)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
285 | unknown
h: error
p: exists a2.(exists a4.(gitaar(a4) & op(a2,a4)) & exists z126.(exists a3.kaal(a3) & persoon(z126) & a2(z126)))
s: error
------------------------------
304 | unknown
h: exists a3.(exists a5.(verf(a5) & met(a3,a5)) & exists a2.(exists a4.jong(a4) & exists a4.topless(a4) & vrouw(a2) & a3(a2)))
p: exists a3.(exists a5.(verf(a5) & met(a3,a5)) & exists a2.(exists a4.oud(a4) & exists a4.topless(a4) & vrouw(a2) & a3(a2)))
s: (FATAL)
%%ERROR: The following symbols are used with multiple arities: met/1, met/2.


Fatal error:  The following symbols are used with multiple arities: met/1, met/2
------------------------------
317 | unknown
h: (buurt(\C.in(\B.exists a2.(exists a3.(menigte(a3) & mens(a2)) & B(a2)),C)) & water(\C.van(\C.in(\B.exists a2.(exists a3.(menigte(a3) & mens(a2)) & B(a2)),C),C)))
p: error
s: error
------------------------------
382 | unknown
h: error
p: (((\A B.A & B)(\B.(exists a5.hoog(a5) & gras(B))))(\A.A(\a2.rennen(a2))))((\Q.exists a4.(exists a5.wit(a5) & hond(a4) & Q(a4)) & \B.exists a3.(bruin(a3) & B(a3))))
s: error
------------------------------
384 | yes
h: (((\A B.A & B)(\B.exists a4.(veld(a4) & B(a4))))(\A.A(\a2.lopen(a2))))((\Q.exists a4.(exists a5.bruingeel(a5) & hond(a4) & Q(a4)) & \B.exists a3.(wit(a3) & B(a3))))
p: exists a2.((\Q.exists a6.(exists a7.groen(a7) & gras(a6) & Q(a6)) & \a5.hoog(a5))(\C.door(a2,C)) & (\Q.exists a4.(exists a5.bruingeel(a5) & hond(a4) & Q(a4)) & \B.exists a3.(wit(a3) & B(a3)))(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
394 | unknown
h: (\B.exists a5.(exists a7.(stuk(a7) & op(a5,a7)) & B(a5)) & \B.exists a4.(exists a6.(fiets(a6) & bij(a4,a6)) & B(a4)))(\B.exists a3.(man(a3) & B(a3)))
p: (\B.exists a4.(exists a5.(brief(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a5.(fiets(a5) & bij(a3,a5)) & B(a3)))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
402 | unknown
h: (((\A B.A & B)(\a4.gras(a4)))(\A.A(\a2.lopen(a2))))(\B.exists a2.(exists a3.(groep(a3) & ontdekkingsreiziger(a2)) & B(a2)))
p: error
s: error
------------------------------
417 | unknown
h: exists a2.(weg(a2) & exists a3.(kant(\C.aan(a3,C)) & exists a8.(besneeuwde(a8) & van(\C.aan(a3,C),a8)) & exists a2.((((\A B.A & B)(\Q.exists a5.(auto(a5) & Q(a5))))(\B.(exists a4.twee(a4) & man(B))))(a2) & a3(a2))))
p: exists a2.(weg(a2) & exists a3.(exists a4.(pauze(a4) & exists a7.(reis(a7) & exists a10.(besneeuwde(a10) & op(a7,a10)) & van(a4,a7)) & a3(a4)) & exists a2.(exists z175.twee(z175) & man(a2) & a3(a2))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (weg(a2) & exists a3 ((kant(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
450 | unknown
h: exists a2.(golf(\C.naar(a2,C)) & exists z196.(exists a3.blond(a3) & meisje(z196) & a2(z196)))
p: error
s: error
------------------------------
520 | unknown
h: error
p: (((\A B.A & B)(\B.exists a4.(fiets(a4) & B(a4))))(exists a4.((\B.exists a7.(exists a8.roze(a8) & sjaal(a7) & B(a7)) & \Q.exists a6.(bottoms(a6) & Q(a6)))(a4) & rijden(a4))))(exists z231.(exists a5.roze(a5) & bell(z231) & (exists a4.exists a5.(exists a6.zilveren(a6) & broek(a5) & exists b.persoon(b)(a5))(a4) & vrouw(a4))(z231)))
s: error
------------------------------
526 | unknown
h: error
p: (((\A B.A & B)(\B.exists a4.(fiets(a4) & B(a4))))(exists a4.((\B.exists a7.(exists a8.roze(a8) & sjaal(a7) & B(a7)) & \Q.exists a6.(bottoms(a6) & Q(a6)))(a4) & rijden(a4))))(exists z231.(exists a5.roze(a5) & bell(z231) & (exists a4.exists a5.(exists a6.zilveren(a6) & broek(a5) & exists b.persoon(b)(a5))(a4) & vrouw(a4))(z231)))
s: error
------------------------------
530 | unknown
h: \B.exists a1.((exists a3.(exists a6.(versnelling(a6) & exists a5.(exists z234.(zwart(z234) & a5(z234)) & a6(a5)))(exists b.persoon(b)))(a3) & motorrijder(a3))(a1) & B(a1))
p: error
s: error
------------------------------
592 | no
h: error
p: error
s: error
------------------------------
619 | unknown
h: error
p: (\B.exists a5.(exists a7.(touw(a7) & aan(a5,a7)) & B(a5)) & \F264.exists a3.(exists a5.(exists a7.((((\A B.A & B)(\Q.exists a10.(((\A B.A & B)(\A B.exists a11.(A(a11) & B(a11))))(a10) & Q(a10))))(\A.A(\z261.bouwen(z261))))(a7) & (exists a8.exists a10.(kunstmatig(a10) & exists b.persoon(b)(a10))(a8) & muur(a8))(a7))(a5) & op(a3,a5)) & F264(a3)))(\B.exists a2.(jongen(a2) & B(a2)))
s: error
------------------------------
630 | no
h: error
p: error
s: error
------------------------------
647 | unknown
h: \F290.exists a1.(exists a3.(rots(a3) & exists z289.((((\A B.A & B)(\Q.exists a6.(exists a7.roze(a7) & klimspull(a6) & Q(a6))))(\A B.(exists a4.A(exists b.persoon(b),a4) & B(a4))))(z289) & a3(z289)))(a1) & F290(a1))
p: (((\A B.A & B)(\B.exists a4.(touw(a4) & B(a4))))(\B.exists a3.(exists a4.(klif(a4) & a3(a4)) & B(a3))))(\Q.exists a2.(exists a3.eén(a3) & man(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F290.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
651 | unknown
h: (((\A B.A & B)(\B.exists a4.(touw(a4) & B(a4))))(\B.exists a3.(exists a4.(klif(a4) & a3(a4)) & B(a3))))(\Q.exists a2.(exists a3.eén(a3) & man(a2) & Q(a2)))
p: error
s: error
------------------------------
687 | unknown
h: (((\A B.A & B)(\B.(overkant(B) & straat(\C.van(B,C)))))(\B.exists a3.(exists z304.(\F305.(exists a5.z304(exists b.persoon(b),a5) & F305(a5)) & naar(a3,z304)) & B(a3))))(\Q.exists a2.((((\A B.A & B)(\Q.exists a5.(exists a6.verschillend(a6) & ras(a5) & Q(a5))))(\B.(exists a4.twee(a4) & hond(B))))(a2) & Q(a2)))
p: exists a2.(staart(a2) & exists a5.zwart(a5) & straat(\C.naar(\B.exists a2.(exists a3.wit(a3) & hond(a2) & B(a2)),C)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
698 | unknown
h: error
p: error
s: error
------------------------------
717 | no
h: exists a1.(entity(a1) & exists a3.((((\A B.A & B)(\B.exists a6.(wedstrijd(a6) & B(a6))))(\B.exists a5.(paar(a5) & man(B))))(a3) & rennen(a3))(a1))
p: ((\A B.A & B)(\F330.exists a3.((\A B.A & B)(a3) & F330(a3))))(\F329.exists a2.((((\A B.A & B)(\B.exists a5.(wedstrijd(a5) & B(a5))))(\B.exists a4.(paar(a4) & man(B))))(a2) & F329(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a1 (%%START ERROR%%entity(a1) & exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
718 | unknown
h: exists a3.(exists a4.(buiten(a4) & a3(a4)) & exists z333.(exists a4.(paar(a4) & man(z333)) & a3(z333)))
p: ((\A B.A & B)(\F330.exists a3.((\A B.A & B)(a3) & F330(a3))))(\F329.exists a2.((((\A B.A & B)(\B.exists a5.(wedstrijd(a5) & B(a5))))(\B.exists a4.(paar(a4) & man(B))))(a2) & F329(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    ((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
765 | unknown
h: error
p: error
s: error
------------------------------
780 | unknown
h: exists a2.(exists a4.(boomstronk(a4) & op(a2,a4)) & (\B.exists a4.(hond(a4) & B(a4)) & \B.exists a3.(vrouw(a3) & B(a3)))(a2))
p: exists a3.(exists z350.(vrouw(z350) & a3(z350)) & (buurt(\C.in(\B.(exists a4.oud(exists b.persoon(b),a4) & B(a4)),C)) & exists a9.(exists a10.wit(a10) & hond(a9) & van(\C.in(\B.(exists a4.oud(exists b.persoon(b),a4) & B(a4)),C),a9)))(a3))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a4 (boomstronk(a4) & op(a2,a4)) & (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
816 | yes
h: exists a3.(exists a5.((exists a7.((((\A B.A & B)(\Q.exists a11.(bescherming(a11) & Q(a11))))(\A.A(\a9.gebruiken(a9))))(exists b.persoon(b)))(a7) & uitrusting(a7))(a5) & met(a3,a5)) & exists a2.(exists z378.(groep(z378) & mens(a2)) & a3(a2)))
p: exists a3.(exists a5.(exists a6.(kleding(a6) & a5(a6)) & met(a3,a5)) & exists a2.(exists z372.(groep(z372) & mens(a2)) & a3(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a3 (exists a5 ((%%START ERROR%%exists a7.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
860 | yes
h: error
p: (((\A B.A & B)(\a4.gras(a4)))(\B.(exists a3.(exists a4.aan(exists b.persoon(b),exists b.persoon(b),a4) & a3(a4)) & B(a3))))((\Q.exists a4.(exists a5.één(a5) & exists a6.zwart(a6) & \F395.exists a6.(a4(a6) & F395(a6)) & Q(a4)) & \Q.exists a3.(exists a4.eén(a4) & exists a5.wit(a5) & hond(a3) & Q(a3))))
s: error
------------------------------
873 | unknown
h: (exists a3.vol(a3) & exists a5.(mens(a5) & met(\F399.exists a2.(((\A B.A & B)(\Q.exists a4.(exists a5.(schaatsbaan(a5) & a4(a5)) & Q(a4))))(a2) & F399(a2)),a5)))
p: exists a4.(schaatspark(a4) & in(\Q.exists a2.(mens(\D.-a2(D)) & Q(a2)),a4))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (exists a3 vol(a3) & exists a5 (mens(a5) & met(%%START ERROR%%\F399.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
882 | unknown
h: (\A B.A & B)(exists a6.(blauwwit(a6) & uniform(\C.in(\B.exists a4.(man(a4) & B(a4)),C)))(\a3.meisje(a3)))
p: error
s: error
------------------------------
913 | no
h: exists a2.(-exists a3.(exists a5.((((\A B.A & B)(\B.exists a8.(man(a8) & B(a8))))(\A.A(\a6.kussen(a6))))(a5) & vrouw(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\A.A(\a3.kussen(a3))))(\B.exists a2.(vrouw(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 (%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
933 | unknown
h: exists a2.(exists a3.(exists a4.gigantisch(a4) & luchtbel(a3) & a2(a3)) & exists a3.jong(a3) & meisje(a2))
p: exists a2.(exists a3.(luchtbel(a3) & a2(a3)) & (((\A B.A & B)(\B.(exists a6.rood(a6) & shirt(B))))(\a3.meisje(a3)))(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 (luchtbel(a3) & a2(a3)) & (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
947 | yes
h: error
p: error
s: error
------------------------------
980 | unknown
h: error
p: error
s: error
------------------------------
987 | no
h: \F445.exists a1.(exists a3.(-exists a4.(exists a6.(exists a7.exists a9.(jongen(a9) & met(exists b.persoon(b),a9))(a7) & a6(a7) & (((\A B.A & B)(\a8.amfitheater(a8)))(\a6.volwassen(a6)))(a6))(a4) & a3(a4)) & exists a2.(entity(a2) & a3(a2)))(a1) & F445(a1))
p: (\B.exists a4.(exists a6.(jongen(a6) & met(a4,a6)) & B(a4)) & \B.amfitheater(\C.in(B,C)))(\B.exists a2.(volwassen(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F445.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
988 | unknown
h: (\B.exists a4.(exists a6.(jongen(a6) & met(a4,a6)) & B(a4)) & \B.amfitheater(\C.in(B,C)))(\B.exists a2.(volwassen(a2) & B(a2)))
p: error
s: error
------------------------------
1039 | unknown
h: error
p: error
s: error
------------------------------
1102 | unknown
h: error
p: exists a2.(exists a4.(paard(a4) & op(a2,a4)) & exists z480.(vrouw(z480) & a2(z480)))
s: error
------------------------------
1137 | unknown
h: exists a2.(vis(a2) & schildpad(a2))
p: exists a4.(zee(a4) & in(((\A B.A & B)(\B.exists a5.(schildpad(a5) & B(a5))))(\B.exists a6.(jacht(a6) & op(B,a6))),a4))(\B.exists a2.(vis(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1170 | unknown
h: exists a4.(schijf(a4) & in(\B.exists a3.(exists a4.(wortel(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(vrouw(a2) & B(a2)))
p: \C.((((\A B.A & B)(\F502.exists a5.((((\A B.A & B)(\Q.exists a8.(schijf(a8) & Q(a8))))(\a6.vrouw(a6)))(a5) & F502(a5))))(\A.A(\a3.snijden(a3))))(\B.exists a2.(aardappel(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1177 | unknown
h: exists z511.(\B.(exists a3.z511(exists b.persoon(b),a3) & B(a3)) & exists a3.(vrouw(a3) & z511(a3)))
p: exists z510.(\B.(exists a3.z510(exists b.persoon(b),a3) & B(a3)) & exists a3.(vrouw(a3) & z510(a3)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists z511 (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1178 | no
h: error
p: exists z510.(\B.(exists a3.z510(exists b.persoon(b),a3) & B(a3)) & exists a3.(vrouw(a3) & z510(a3)))
s: error
------------------------------
1190 | yes
h: (((\A B.A & B)(\a4.bos(a4)))(exists a3.(entity(a3) & a3(\z514.lopen(z514)))))((\B.exists a4.(vrouw(a4) & B(a4)) & \Q.exists a3.(man(a3) & Q(a3))))
p: (((\A B.A & B)(\B.exists a4.(exists a5.bosrijk(a5) & omgeving(a4) & B(a4))))(\A.A(\a2.wandelen(a2))))((\B.exists a4.(vrouw(a4) & B(a4)) & \Q.exists a3.(man(a3) & Q(a3))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1192 | yes
h: (((\A B.A & B)(\B.exists a4.(exists a5.bosrijk(a5) & omgeving(a4) & B(a4))))(\A.A(\a2.lopen(a2))))((\B.exists a4.(vrouw(a4) & B(a4)) & \Q.exists a3.(man(a3) & Q(a3))))
p: (((\A B.A & B)(\a4.bos(a4)))(exists a3.(entity(a3) & a3(\z514.lopen(z514)))))((\B.exists a4.(vrouw(a4) & B(a4)) & \Q.exists a3.(man(a3) & Q(a3))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1232 | unknown
h: exists a4.(schijf(a4) & in(\B.exists a3.(exists a4.(tomaat(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(man(a2) & B(a2)))
p: \F523.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(snee(a6) & in(\B.exists a5.(exists a6.(brood(a6) & a5(a6)) & B(a5)),a6))))(\B.exists a3.(man(a3) & B(a3))))(a1) & F523(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1236 | no
h: (((\A B.A & B)(\Q.exists a4.(exists a5.ander(a5) & vrouw(a4) & Q(a4))))((\A.A(\a4.zingen(a4)) & \A.A(\a3.dansen(a3)))))(\B.exists a2.(vrouw(a2) & B(a2)))
p: (exists a4.(entity(a4) & a4(\z532.zingen(z532))) & \A.A(\a2.dansen(a2)))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1237 | unknown
h: (regen(\C.in(\A.A(\a4.zingen(a4)),C)) & \A.A(\a2.dansen(a2)))(\B.exists a2.(vrouw(a2) & B(a2)))
p: error
s: error
------------------------------
1241 | unknown
h: (regen(\C.in(\A.A(\a4.zingen(a4)),C)) & \A.A(\a2.dansen(a2)))(\B.exists a2.(vrouw(a2) & B(a2)))
p: (((\A B.A & B)(\Q.exists a4.(exists a5.ander(a5) & vrouw(a4) & Q(a4))))((\A.A(\a4.zingen(a4)) & \A.A(\a3.dansen(a3)))))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (regen(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1266 | yes
h: exists a2.(podium(\C.op(a2,C)) & exists z542.(band(z542) & a2(z542)))
p: (((\A B.A & B)(\B.exists a4.(podium(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\B.exists a2.(band(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (podium(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1302 | unknown
h: (((\A B.A & B)(\B.exists a4.(bal(a4) & B(a4))))(\B.exists a3.(exists a4.(spel(a4) & a3(a4)) & B(a3))))(\B.exists a2.(man(a2) & B(a2)))
p: \B.exists a1.(exists a3.(man(a3) & spelen(a3))(a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1333 | yes
h: \C.((((\A B.A & B)(\B.exists a5.(exists a6.ander(a6) & vrouw(a5) & B(a5))))(\A.A(\a3.meten(a3))))(\B.exists a2.(vrouw(a2) & B(a2))))(C)
p: exists a2.(exists a4.ander(a4) & vrouw(a2) & vrouw(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1390 | unknown
h: \F590.exists a1.(exists a3.(exists a4.((((\A B.A & B)(\A.A))(\a5.ui(a5)))(a4) & a3(a4)) & exists z589.(persoon(z589) & a3(z589)))(a1) & F590(a1))
p: exists a2.(buurt(\C.in(a2,C)) & exists a7.(motorfiets(a7) & van(\C.in(a2,C),a7)) & exists z591.(persoon(z591) & a2(z591)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F590.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1396 | unknown
h: exists a2.(man(a2) & bang(a2))
p: exists a2.(man(a2) & schreeuwen(a2))
s:False | False 
------------------------------
1400 | unknown
h: exists a2.(man(a2) & schreeuwen(a2))
p: exists a2.(exists a3.triest(a3) & man(a2) & huilen(a2))
s:False | False 
------------------------------
1410 | unknown
h: exists a4.(exists a5.klein(a5) & bakje(a4) & in(exists a5.(boter(a5) & \F595.exists z596.(aan(a5,z596) & F595(z596))),a4))(\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(exists a3.(garnaal(a3) & a2(a3)) & exists z598.(vrouw(z598) & a2(z598)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1412 | yes
h: \B.exists a1.(exists a3.(exists a4.(hout(a4) & \C.aan(a4,C) & a3(a4)) & exists z600.(man(z600) & a3(z600)))(a1) & B(a1))
p: \B.exists a1.(exists a3.(exists a4.(houtblok(a4) & \C.aan(a4,C) & a3(a4)) & exists z599.(man(z599) & a3(z599)))(a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1443 | unknown
h: exists a2.(man(a2) & spugen(a2))
p: exists a2.(radio(\C.op(a2,C)) & exists z618.(man(z618) & a2(z618)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (radio(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1469 | no
h: (buurt(\C.in((\A.A(\a6.schoppen(a6)) & \A.A(\a5.springen(a5)))(\B.exists a4.(-exists a5.((exists a7.(exists b.persoon(b)(\a7.rennen(a7)))(a7) & man(a7))(a5) & a4(a5)) & B(a4))),C)) & exists z626.(verkoopautomaat(z626) & van(\C.in((\A.A(\a6.schoppen(a6)) & \A.A(\a5.springen(a5)))(\B.exists a4.(-exists a5.((exists a7.(exists b.persoon(b)(\a7.rennen(a7)))(a7) & man(a7))(a5) & a4(a5)) & B(a4))),C),z626)))(\A.exists a1.(entity(a1) & A(a1)))
p: error
s: error
------------------------------
1470 | unknown
h: error
p: (\A B.A & B)(exists a3.(exists a5.(muur(a5) & van(a3,a5)) & exists z624.(exists a4.drie(a4) & man(z624) & a3(z624))))
s: error
------------------------------
1487 | no
h: exists a3.(saus(a3) & kip(\C.voor(a3,C)))(\a2.man(a2))
p: error
s: error
------------------------------
1493 | yes
h: exists a2.(exists a3.(gitaar(a3) & a2(a3)) & exists z631.(man(z631) & a2(z631)))
p: exists a2.(exists a4.(exists a5.elektrisch(a5) & gitaar(a4) & op(a2,a4)) & exists z616.(man(z616) & a2(z616)))
s:False | False 
------------------------------
1495 | yes
h: (((\A B.A & B)(\B.exists a4.(gitaar(a4) & B(a4))))(\A.A(\a2.tokkelen(a2))))(\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(exists a4.(gitaar(a4) & op(a2,a4)) & exists z486.(man(z486) & a2(z486)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1503 | no
h: \F633.exists a1.(aan(\Q.exists a3.((((\A B.A & B)(\Q.exists a6.(karatekostuum(a6) & Q(a6))))(\B.(exists a5.drie(a5) & jongen(B))))(a3) & Q(a3)),a1) & F633(a1))
p: \F634 C.F634(\D.-(exists a3.((((\A B.A & B)(\Q.exists a6.(karatekostuum(a6) & Q(a6))))(\B.(exists a5.drie(a5) & jongen(B))))(a3) & vechten(a3))(\E.E(D)))(C))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F633.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1506 | unknown
h: \F633.exists a1.(aan(\Q.exists a3.((((\A B.A & B)(\Q.exists a6.(karatekostuum(a6) & Q(a6))))(\B.(exists a5.drie(a5) & jongen(B))))(a3) & Q(a3)),a1) & F633(a1))
p: ((\A B.A & B)(\A.A(\a3.oefenen(a3))))(\Q.exists a3.(exists a4.drie(a4) & man(a3) & Q(a3)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F633.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1525 | unknown
h: exists a3.(vrouw(a3) & snijden(a3))
p: exists a2.(exists a3.(bloem(a3) & a2(a3)) & exists z646.(exists a3.(vrouw(a3) & plant(z646)) & a2(z646)))
s:False | False 
------------------------------
1584 | yes
h: \B.exists a1.(exists a3.(exists a4.(exists a5.slim(a5) & aarde(\C.in(a4,C)) & a3(a4)) & das(a3))(a1) & B(a1))
p: exists a2.(exists a3.(exists a5.((((\A B.A & B)(\a8.das(a8)))(\A.A(\a6.graven(a6))))(a5) & gat(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1608 | no
h: error
p: error
s: error
------------------------------
1628 | unknown
h: error
p: \C.exists a3.(exists a5.((((\A B.A & B)(\B.exists a8.(kom(a8) & B(a8))))(\a6.persoon(a6)))(a5) & door(a3,a5)) & exists a2.(ingrediënt(a2) -> a3(a2)))(C)
s: error
------------------------------
1676 | unknown
h: \C.((((\A B.A & B)(\a5.man(a5)))(\A.A(\a3.bespelen(a3))))(\a2.gitaar(a2)))(C)
p: \B.exists a1.(exists a3.(exists a4.vredig(a4) & water(\C.over(a3,C)) & exists z706.(boot(z706) & \F705.exists z706.(a3(z706) & F705(z706))))(a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1690 | yes
h: error
p: \C.((((\A B.A & B)(\B.exists a5.(kat(a5) & B(a5))))(\A.A(\a3.drinken(a3))))(\a2.melk(a2)))(C)
s: error
------------------------------
1703 | yes
h: \F726.exists a1.(exists a3.(exists a4.((((\A B.A & B)(\A.A))(\B.(container(B) & exists a8.(plastic(a8) & van(B,a8)))))(a4) & a3(a4)) & exists z725.(man(z725) & a3(z725)))(a1) & F726(a1))
p: error
s: error
------------------------------
1711 | unknown
h: \B.(exists a1.vast(a1) & exists a3.(exists a4.achteloos(a4) & exists a5.(kikker(a5) & a3(a5)) & exists z728.(man(z728) & a3(z728)))(B))
p: \F726.exists a1.(exists a3.(exists a4.((((\A B.A & B)(\A.A))(\B.(container(B) & exists a8.(plastic(a8) & van(B,a8)))))(a4) & a3(a4)) & exists z725.(man(z725) & a3(z725)))(a1) & F726(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1754 | yes
h: \C.((((\A B.A & B)(\B.exists a5.(meisje(a5) & B(a5))))(\A.A(\a3.bespelen(a3))))(\B.exists a2.(fluit(a2) & B(a2))))(C)
p: \C.((((\A B.A & B)(\B.exists a5.(exists a6.mooi(a6) & manier(a5) & B(a5))))(((\A B.A & B)(\B.exists a6.(meisje(a6) & B(a6))))(\A.A(\a4.bespelen(a4)))))(\B.exists a2.(fluit(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1807 | unknown
h: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\A.A(\a3.bespelen(a3))))(\B.exists a2.(fluit(a2) & B(a2))))(C)
p: (exists a3.luid(a3) & ((\A B.A & B)(\a5.gitaar(a5)))(\A.A(\a2.spelen(a2))))(\a2.volwassen(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1811 | unknown
h: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\B C.B(\D.-bespelen(D,C))))(\B.exists a2.(fluit(a2) & B(a2))))(C)
p: (((\A B.A & B)(\a4.gitaar(a4)))(\B.(exists a3.luid(a3) & B(\a3.spelen(a3)))))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1839 | yes
h: error
p: error
s: error
------------------------------
1847 | unknown
h: error
p: exists a2.(stoel(\C.op(a2,C)) & exists z786.(exists a3.eén(a3) & man(z786) & a2(z786)))
s: error
------------------------------
1861 | unknown
h: microfoon(\C.in(\A.A(\a2.praten(a2)),C),\a2.papegaai(a2))
p: \C.(microfoon(\a2.dempen(a2)) & exists a6.(papegaai(a6) & voor(\a2.dempen(a2),a6)))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    microfoon(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1877 | unknown
h: \C.((((\A F796.A & B)(\a5.kittens(a5)))(\A.A(\a3.opeten(a3))))(((\A B.A & B)(\a5.dienblad(a5)))(\a3.voedsel(a3))))(C)
p: error
s: error
------------------------------
1881 | yes
h: \F793.exists a4.(aan(\B.exists a2.(exists a3.(paar(a3) & kittens(a2)) & B(a2)),a4) & F793(a4))
p: \C.((((\A F796.A & B)(\a5.kittens(a5)))(\A.A(\a3.opeten(a3))))(((\A B.A & B)(\a5.dienblad(a5)))(\a3.voedsel(a3))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F793.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
1964 | yes
h: (\A.A(\a3.zingen(a3)) & \B.exists a3.(exists a4.(gitaar(a4) & a3(a4)) & B(a3)))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: (\A.A(\a3.zingen(a3)) & \B.exists a3.(exists a4.(gitaar(a4) & a3(a4)) & B(a3)))(\Q.exists a2.(exists a3.eén(a3) & persoon(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2001 | yes
h: exists a2.(paard(\C.op(a2,C)) & exists z833.(man(z833) & a2(z833)))
p: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\A.A(\a3.berijden(a3))))(\a2.paard(a2)))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (paard(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2019 | unknown
h: (((\A B.A & B)(\B.exists a4.(boom(a4) & B(a4))))(\B.exists a3.(exists a4.(fiets(a4) & a3(a4)) & B(a3))))(\F840.exists a2.((((\A B.A & B)(\Q.exists a5.(mes(a5) & Q(a5))))(\B.(exists a4.gevaarlijk(a4) & man(B))))(a2) -> F840(a2)))
p: exists a3.(exists a4.(exists a5.gevaarlijk(a5) & mes(a4) & a3(a4)) & exists a4.(boom(a4) & naar(a3,a4)))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2058 | yes
h: exists a2.((((\A B.A & B)(\Q.exists a6.(exists a8.((((\A B.A & B)(\B.exists a11.(vrouw(a11) & B(a11))))(\A.A(\a9.snijden(a9))))(a8) & stuk(a8))(a6) & Q(a6))))(\a4.vlees(a4)))(a2) & exists a1.(entity(a1) & a2(a1)))
p: \F853.exists a1.(exists a3.(exists a4.precies(a4) & (((\A B.A & B)(\A.A))(\a6.vlees(a6)))(a3) & exists z852.(dame(z852) & a3(z852)))(a1) & F853(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2089 | no
h: exists a2.(exists a3.(interview(a3) & a2(a3)) & man(a2))
p: error
s: error
------------------------------
2096 | unknown
h: \B.exists a1.(exists a5.(man(a5) & van(\B.(exists a4.wit(a4) & auto(B)),a5))(a1) & B(a1))
p: exists a2.(exists a3.(interview(a3) & a2(a3)) & man(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2130 | unknown
h: exists a2.(exists a4.(hond(a4) & met(a2,a4)) & exists z906.(exists a3.klein(a3) & jongen(z906) & a2(z906)))
p: exists a2.(exists a3.((((\A B.A & B)(\A B.exists a6.(A(a6) & B(a6))))(\a4.hond(a4)))(a3) & a2(a3)) & exists z909.(exists a3.klein(a3) & jongen(z909) & a2(z909)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2157 | unknown
h: exists a2.(exists a3.(foto(a3) & exists z913.(\B.(exists a6.z913(exists b.persoon(b),a6) & B(a6)) & van(a3,z913)) & a2(a3)) & exists z914.(man(z914) & a2(z914)))
p: (((\A B.A & B)(\Q.exists a4.(zonsondergang(a4) & Q(a4))))(\F924 C.((((\A B.A & B)(\B.exists a6.(man(a6) & strand(\C.op(a6,C)) & B(a6))))(\A.A(\a4.maken(a4))))(F924))(C)))(\B.(foto(B) & exists a5.(exists a6.(camera(a6) & a5(a6)) & van(B,a5))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 ((foto(a3) & exists z913 (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2166 | yes
h: error
p: (((\A B.A & B)(\B.exists a4.(machine(a4) & B(a4))))(\A.A(\a2.naaien(a2))))(\B.exists a2.(vrouw(a2) & B(a2)))
s: error
------------------------------
2221 | unknown
h: \B.exists a1.(man(\D.-exists a6.(paard(a6) & van(\E.E(D),a6))(a1)) & B(a1))
p: exists z957.(exists a4.(paard(a4) & van(z957,a4)) & exists z956.(\B.(exists a2.z956(exists b.persoon(b),a2) & B(a2)) & z957(z956)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2229 | unknown
h: \F963.exists a1.(((((\A B.A & B)(\B.exists a5.(tafel(a5) & B(a5))))(\B.exists a4.(exists a5.(vinger(a5) & exists b.persoon(b)(a5)) & a4(a5) & B(a4))))(\B.exists a3.(vrouw(a3) & B(a3))))(a1) & F963(a1))
p: (((\A B.A & B)(\B.exists a4.(tafel(a4) & B(a4))))(\B.exists a3.(exists a5.(vinger(a5) & exists b.persoon(b)(a5)) & met(a3,a5) & B(a3))))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F963.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2231 | unknown
h: \F963.exists a1.(((((\A B.A & B)(\B.exists a5.(tafel(a5) & B(a5))))(\B.exists a4.(exists a5.(vinger(a5) & exists b.persoon(b)(a5)) & a4(a5) & B(a4))))(\B.exists a3.(vrouw(a3) & B(a3))))(a1) & F963(a1))
p: exists a2.(exists a4.(vinger(a4) & exists b.persoon(b)(a4)) & op(a2,a4) & exists z962.(vrouw(z962) & a2(z962)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F963.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2284 | yes
h: (spelen(\C.aan(\a2.kat(a2),C)) & exists a7.(watermeloen(a7) & met(\C.aan(\a2.kat(a2),C),a7)))
p: error
s: error
------------------------------
2286 | yes
h: exists a2.(exists a4.(watermeloen(a4) & met(a2,a4)) & exists z983.(kat(z983) & a2(z983)))
p: error
s: error
------------------------------
2362 | unknown
h: exists a4.(brand(a4) & in(\B.exists a3.(camera(a3) & B(a3)),a4))(\B.(exists a3.lang(a3) & persoon(B)))
p: exists a3.(camera(a3) & exists a4.(gasbrander(a4) & met(a3,a4)))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2364 | yes
h: exists a4.(brand(a4) & in(\B.exists a3.(camera(a3) & B(a3)),a4))(\a2.persoon(a2))
p: error
s: error
------------------------------
2366 | unknown
h: exists a4.(brand(a4) & in(\B.exists a3.(camera(a3) & B(a3)),a4))(\a2.persoon(a2))
p: \F1000.exists a1.(exists a3.(exists a4.(exists a6.(exists a7.(fakkel(a7) & a6(a7)) & op(a4,a6)) & a3(a4)) & (((\A B.A & B)(\B.exists a5.(exists a6.(aantal(a6) & exists a7.(camera(a7) & a5(a7))) & B(a5))))(\a3.persoon(a3)))(a3))(a1) & F1000(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2385 | unknown
h: exists a4.(stuk(a4) & in(\B.exists a3.(exists a4.(wortel(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(persoon(a2) & B(a2)))
p: exists a4.(stuk(a4) & in(\B.exists a3.(exists a4.(ui(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(persoon(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2392 | no
h: \F1017.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B.exists a5.(exists a6.(aardappel(a6) & a5(a6)) & B(a5)),a6))))(\a3.man(a3)))(a1) & F1017(a1))
p: \F1022.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B C.B(\D.-exists a6.(aardappel(a6) & a6(D))(C)),a6))))(\a3.man(a3)))(a1) & F1022(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F1017.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2402 | unknown
h: \B.(exists a1.vast(a1) & exists a3.(exists a4.(exists a5.heel(a5) & tomaat(a4) & a3(a4)) & vrouw(a3))(B))
p: exists a2.(exists a3.(tomaat(a3) & a2(a3)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2404 | no
h: error
p: \F1023.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B.exists a5.(exists a6.(tomaat(a6) & a5(a6)) & B(a5)),a6))))(\a3.dame(a3)))(a1) & F1023(a1))
s: error
------------------------------
2405 | yes
h: exists a2.(exists a3.(tomaat(a3) & a2(a3)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
p: \F1023.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B.exists a5.(exists a6.(tomaat(a6) & a5(a6)) & B(a5)),a6))))(\a3.dame(a3)))(a1) & F1023(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (%%START ERROR%%exists a3 (tomaat(a3) & a2(a3)) & \B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2410 | unknown
h: \C.((((\A B.A & B)(\B.exists a5.(mes(a5) & exists a8.(schijf(a8) & in(a5,a8)) & B(a5))))(((\A B.A & B)(\a6.vrouw(a6)))(\A.A(\a4.snijden(a4)))))(\B.exists a2.(ui(a2) & B(a2))))(C)
p: error
s: error
------------------------------
2430 | yes
h: \B.exists a1.(aan(\B.exists a3.(man(a3) & B(a3)),a1) & B(a1))
p: error
s: error
------------------------------
2476 | yes
h: exists a2.(exists a3.(groep(a3) & mens(a2)) & zingen(a2))
p: exists a2.(mens(a2) -> zingen(a2))
s:True | False 
------------------------------
2485 | unknown
h: exists a2.(trompet(a2) & exists a2.(man(a2) & spelen(a2)))
p: exists a2.(exists a3.(gitaar(a3) & a2(a3)) & man(a2))
s:False | False 
------------------------------
2525 | unknown
h: (((\A B.A & B)(\B.exists a6.(vlot(a6) & B(a6))))(\A.A(\a4.peddelen(a4))) & \A.A(\a2.rijden(a2)))(\Q.exists a2.(mens(a2) & Q(a2)))
p: (((\A B.A & B)(\B.exists a4.(vlot(a4) & B(a4))))(\A.A(\a2.drijven(a2))))(\B.exists a2.(exists a3.(paar(a3) & mens(a2)) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2527 | unknown
h: (((\A B.A & B)(\B.exists a4.(vlot(a4) & B(a4))))(\A.A(\a2.drijven(a2))))(\Q.exists a2.(exists a3.vi(a3) & mens(a2) & Q(a2)))
p: (((\A B.A & B)(\B.exists a6.(vlot(a6) & B(a6))))(\A.A(\a4.peddelen(a4))) & \A.A(\a2.rijden(a2)))(\Q.exists a2.(mens(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2535 | unknown
h: exists a2.(maïs(a2) & exists z1060.(kat(z1060) & a2(z1060)))
p: exists a2.(-exists a3.((exists a5.((((\A B.A & B)(\a8.kolf(a8)))(\B.exists a7.(exists a8.(maïs(a8) & a7(a8)) & B(a7))))(exists b.persoon(b)))(a5) & kat(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: 'utf-8' codec can't decode byte 0xc3 in position 587: invalid continuation byte
------------------------------
2544 | unknown
h: exists a4.(schijf(a4) & in(\B.exists a3.(exists a4.(tomaat(a4) & a3(a4)) & B(a3)),a4))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: \F1063.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B.exists a5.(exists a6.(groente(a6) & a5(a6)) & B(a5)),a6))))(\a3.persoon(a3)))(a1) & F1063(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2557 | yes
h: exists a2.(gitaar(a2) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
p: (((\A B.A & B)(\a4.gitaar(a4)))(\A.A(\a2.tokkelen(a2))))(\Q.exists z1069.(\B.(exists a2.z1069(exists b.persoon(b),a2) & B(a2)) & Q(z1069)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (%%START ERROR%%gitaar(a2) & \B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2566 | yes
h: \F1071.exists a4.(aan(\B.exists a2.(exists a3.(paar(a3) & vrouw(a2)) & B(a2)),a4) & F1071(a4))
p: \F1070.exists a4.(aan(\Q.exists a2.(exists a3.drie(a3) & vrouw(a2) & Q(a2)),a4) & F1070(a4))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F1071.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2604 | yes
h: error
p: \C.exists a3.(aap(\C.door(a3,C)) & exists a2.(bulldog(a2) & a3(a2)))(C)
s: error
------------------------------
2606 | unknown
h: exists a2.(aap(a2) & \F1079.exists a6.(aan(a2,a6) & F1079(a6)) & exists z1080.(bulldog(z1080) & a2(z1080)))
p: error
s: error
------------------------------
2662 | unknown
h: \F1096.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(plak(a6) & in(\B.exists a5.(vlees(a5) & B(a5)),a6))))(\a3.dame(a3)))(a1) & F1096(a1))
p: (((\A B.A & B)(\a4.mixer(a4)))(\B.exists a3.(-exists a4.(ei(a4) & a3(a4)) & B(a3))))(\a2.dame(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F1096.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2668 | unknown
h: \Q.exists a1.((((\A B.A & B)(\Q.exists a4.(beneden(a4) & Q(a4))))(exists a4.(exists a5.(exists a7.(plank(a7) & van(a5,a7)) & a4(a5)) & fret(a4))))(a1) & Q(a1))
p: exists a2.(kooi(\C.uit(a2,C)) & exists z1098.(exists a3.(paar(a3) & fret(z1098)) & a2(z1098)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\Q.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2678 | yes
h: exists a4.(auto(a4) & in(\A.A(\a2.stappen(a2)),a4))(\B.exists a2.(man(a2) & B(a2)))
p: exists a4.(garage(a4) & in(exists a5.(auto(a5) & in(\B.(exists a4.haastig(a4) & B(\a4.stappen(a4))),a5)),a4))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2679 | unknown
h: exists a4.(auto(a4) & in(\A.A(\a2.stappen(a2)),a4))(\B.exists a2.(man(a2) & B(a2)))
p: exists a4.(garage(a4) & in(\B.exists a3.(exists a4.(auto(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2687 | no
h: error
p: exists a2.(exists a3.((((\A B.A & B)(\Q.exists a6.(stuk(a6) & Q(a6))))(\B.exists a5.(teen(a5) & knoflook(B))))(a3) & a2(a3)) & persoon(a2))
s: error
------------------------------
2704 | yes
h: exists a4.(water(a4) & in(\B.exists a3.(exists a4.(noedels(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(vrouw(a2) & B(a2)))
p: \C.((((\A B.A & B)(\F1111.exists a5.((((\A B.A & B)(\Q.exists a8.(water(a8) & Q(a8))))(\a6.vrouw(a6)))(a5) & F1111(a5))))(\A.A(\a3.koken(a3))))(\Q.exists a2.(noedels(a2) & Q(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2712 | no
h: error
p: error
s: error
------------------------------
2720 | unknown
h: error
p: (((\A B.A & B)(\B.exists a4.(trainer(a4) & B(a4))))(\A.A(\a2.kickbokst(a2))))(\a2.man(a2))
s: error
------------------------------
2721 | unknown
h: error
p: (((\A B.A & B)(\B.exists a4.(trainer(a4) & B(a4))))(\A.A(\a2.kickbokst(a2))))(\a2.man(a2))
s: error
------------------------------
2722 | yes
h: (\B.exists a4.(exists a5.(gitaar(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a4.(lied(a4) & a3(a4)) & B(a3)))(\B.exists a2.(exists a3.(vrouw(a3) & a2(a3)) & B(a2)))
p: error
s: error
------------------------------
2726 | unknown
h: error
p: (\B.exists a4.(exists a5.(boek(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a5.(deken(a5) & op(a3,a5)) & B(a3)))(\F1114.exists a2.((((\A B.A & B)(\B.exists a5.(rots(a5) & B(a5))))(\a3.vrouw(a3)))(a2) & F1114(a2)))
s: error
------------------------------
2738 | unknown
h: exists a2.(exists a4.(exists a5.akoestisch(a5) & gitaar(a4) & op(a2,a4)) & exists z1118.(man(z1118) & a2(z1118)))
p: error
s: error
------------------------------
2766 | unknown
h: exists a2.(a2(\z1131.blij(z1131)) & (\B.exists a4.(vrouw(a4) & B(a4)) & \Q.exists a3.(man(a3) & Q(a3)))(a2))
p: (\B.exists a3.(exists a5.(a5(\z1132.praten(z1132)) & vrouw(a5))(a3) & B(a3)) & \Q.exists a2.(man(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (a2(%%START ERROR%%\z1131.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2772 | yes
h: exists a4.(pot(a4) & in(\B.exists a3.(exists a4.(bakolie(a4) & a3(a4)) & B(a3)),a4))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: exists a3.(exists a4.(olie(a4) & a3(a4)) & exists a4.(((\A B.A & B)(((\A B.A & B)(\B.exists a8.(pot(a8) & B(a8))))(\A B.exists a6.(A(a6) & B(a6)))))(a4) & om(a3,a4)))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2791 | yes
h: error
p: error
s: error
------------------------------
2795 | yes
h: exists a2.(exists a3.(wortel(a3) & a2(a3)) & exists z1142.(cavia(z1142) & a2(z1142)))
p: error
s: error
------------------------------
2812 | unknown
h: (\A B.A & B)(exists a3.(exists a4.(vliegtuig(a4) & a3(a4)) & stijgen(a3)))
p: exists a2.(vliegtuig(a2) & landen(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2822 | unknown
h: exists a3.(exists a4.(exists a6.(a6(\z1148.klaar(z1148)) & ei(a6))(a4) & a3(a4)) & exists a4.(koekenpan(a4) & in(a3,a4)))(\B.exists a2.(vrouw(a2) & B(a2)))
p: exists a3.(exists a4.(mengsel(a4) & a3(a4)) & exists a4.(\B.exists z1159.(a4(z1159) & B(z1159)) & uit(a3,a4)))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2829 | yes
h: ((\A B.A & B)(\B.exists a3.(exists a4.(oogschaduw(a4) & a3(a4)) & B(a3))))(\a2.vrouw(a2))
p: error
s: error
------------------------------
2842 | unknown
h: exists a2.(piano(\C.op(a2,C)) & exists z1162.(meisje(z1162) & a2(z1162)))
p: (((\A B.A & B)(\a4.podium(a4)))(\B.exists a3.(exists a5.(vleugel(a5) & op(a3,a5)) & B(a3))))(\B.exists a2.(exists a3.klein(a3) & meisje(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (piano(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2886 | no
h: error
p: exists a2.(exists a4.(fluit(a4) & op(a2,a4)) & exists z1182.(vrouw(z1182) & a2(z1182)))
s: error
------------------------------
2898 | yes
h: (\A B.A & B)(exists a3.(exists a4.(gewicht(a4) & a3(a4)) & man(a3)))
p: (\A B.A & B)(exists a3.(exists a4.(halter(a4) & a3(a4)) & man(a3)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2911 | no
h: error
p: (\A B.A & B)(exists a3.(exists a4.(makeup(a4) & a3(a4)) & exists z1196.(vrouw(z1196) & a3(z1196))))
s: error
------------------------------
2932 | unknown
h: \C.((((\A B.A & B)(\B.exists a5.(vrouw(a5) & B(a5))))(((\A B.A & B)(\Q.exists a6.(schijf(a6) & Q(a6))))(\A.A(\a4.snijden(a4)))))(\B.exists a2.(ui(a2) & B(a2))))(C)
p: exists a2.(exists a3.(wortel(a3) & a2(a3)) & vrouw(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2936 | unknown
h: exists a3.(exists a4.(buiten(a4) & a3(a4)) & exists z1207.(veestal(z1207) & a3(z1207)))(\Q.exists a2.(exists a3.twee(a3) & man(a2) & Q(a2)))
p: error
s: error
------------------------------
2965 | unknown
h: (\A B.A & B)(exists a3.(exists a4.(aardappel(a4) & a3(a4)) & exists z1216.(exists a4.groot(a4) & exists a5.groen(a5) & bal(z1216) & a3(z1216))))
p: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1217.(exists a3.groot(a3) & exists a4.groen(a4) & bal(z1217) & a2(z1217)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
2967 | yes
h: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1220.(exists a3.groot(a3) & exists a4.groen(a4) & exists a5.(bal(a5) & z1220(a5)) & a2(z1220)))
p: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1219.(exists a3.groot(a3) & exists a4.groen(a4) & bal(z1219) & a2(z1219)))
s:False | False 
------------------------------
2968 | unknown
h: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1219.(exists a3.groot(a3) & exists a4.groen(a4) & bal(z1219) & a2(z1219)))
p: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1217.(exists a3.groot(a3) & exists a4.groen(a4) & bal(z1217) & a2(z1217)))
s:True | False 
------------------------------
2972 | no
h: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1217.(exists a3.groot(a3) & exists a4.groen(a4) & bal(z1217) & a2(z1217)))
p: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1219.(exists a3.groot(a3) & exists a4.groen(a4) & bal(z1219) & a2(z1219)))
s:True | False 
------------------------------
2996 | unknown
h: exists a1.(entity(a1) & exists a3.(exists a4.(gitaar(a4) & a3(a4)) & exists z1227.(man(z1227) & a3(z1227)))(a1))
p: exists a2.(exists a4.(gitaar(a4) & op(a2,a4)) & exists z486.(man(z486) & a2(z486)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a1 (%%START ERROR%%entity(a1) & exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3002 | unknown
h: exists a1.(entity(a1) & exists a3.(exists a4.(gitaar(a4) & a3(a4)) & exists z1227.(man(z1227) & a3(z1227)))(a1))
p: exists a2.(exists a4.(exists a5.elektrisch(a5) & gitaar(a4) & op(a2,a4)) & exists z1228.(vrouw(z1228) & a2(z1228)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a1 (%%START ERROR%%entity(a1) & exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3036 | no
h: exists a2.(exists a4.(exists a5.plastic(a5) & bakje(a4) & met(a2,a4)) & pup(a2))
p: error
s: error
------------------------------
3061 | no
h: error
p: error
s: error
------------------------------
3107 | unknown
h: (((\A B.A & B)(\B.exists a4.(gitaar(a4) & B(a4))))((\Q.exists a7.(\B.exists z1262.(a7(z1262) & B(z1262)) & Q(a7)) & \B.exists a6.(kamer(a6) & B(a6)))(\C.in(\B.exists a4.(vloer(\C.op(a4,C)) & B(a4)),C))))(\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(exists a3.((((\A B.A & B)(\A B.exists a6.(A(a6) & B(a6))))(\B.exists a5.(gitarist(a5) & B(a5))))(a3) & a2(a3)) & exists z1260.(man(z1260) & a2(z1260)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3122 | yes
h: error
p: error
s: error
------------------------------
3123 | no
h: error
p: error
s: error
------------------------------
3143 | unknown
h: exists a2.(exists a3.(vechtsport(a3) & a2(a3)) & aap(a2))
p: exists a2.(exists a4.(handschoen(a4) & exists b.persoon(b)(a4)) & tegen(a2,a4) & exists z1270.(aap(z1270) & a2(z1270)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((exists a4 (%%START ERROR%%handschoen(a4) & exists b.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3174 | unknown
h: exists a2.(exists a3.(blaasinstrument(a3) & a2(a3)) & exists z1280.(jongen(z1280) & a2(z1280)))
p: exists a2.(entity(a2) & exists a3.(exists a4.(instrument(a4) & a3(a4)) & a2(a3)))(\B.exists a2.(kind(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a2.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3181 | unknown
h: error
p: bos(\C.in(\B F1282.exists a5.(aan(B,a5) & F1282(a5)),C),\B.exists a2.(man(a2) & B(a2)))
s: error
------------------------------
3222 | no
h: exists a2.(exists a4.(brug(a4) & over(a2,a4)) & exists z1302.(jongen(z1302) & a2(z1302)))
p: exists a2.(-exists a3.((exists a5.exists a6.(exists a8.(brug(a8) & over(a6,a8)) & exists b.persoon(b)(a6))(a5) & jongen(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3250 | yes
h: (((\A B.A & B)(\Q.exists a4.(water(a4) & Q(a4))))(exists a5.(pot(a5) & in(\B.exists a4.(exists a5.(exists a6.twee(a6) & ei(a5) & a4(a5)) & B(a4)),a5))))(\B.exists a2.(vrouw(a2) & B(a2)))
p: (((\A B.A & B)(\Q.exists a4.(water(a4) & Q(a4))))(exists a5.(pot(a5) & in(\B.exists a4.(exists a5.(exists a6.twee(a6) & ei(a5) & a4(a5)) & B(a4)),a5))))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3258 | no
h: exists a2.(exists a3.(gitaar(a3) & a2(a3)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
p: exists a2.(gitaar(\C.op(a2,C)) & exists z661.(man(z661) & a2(z661)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (%%START ERROR%%exists a3 (gitaar(a3) & a2(a3)) & \B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3275 | yes
h: exists a4.(\F1314.oceaangolv(\C.uit(F1314,C)) & a4 & in(\A.A(\a2.lopen(a2)),a4))(\B.exists a2.(kind(a2) & B(a2)))
p: exists a4.((\F1312.golf(\C.uit(F1312,C)) & \F1313.oceaan(\C.van(F1313,C)))(a4) & in(\A.A(\a2.lopen(a2)),a4))(\B.exists a2.(kind(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3291 | unknown
h: (((\A B.A & B)(\A B.exists a4.(A(a4) & B(a4))))(\B.exists a3.(exists a4.(varkenskotelet(a4) & a3(a4)) & B(a3))))(\B.exists a2.(vrouw(a2) & B(a2)))
p: exists a2.(entity(a2) & exists a3.(exists a4.(wortel(a4) & a3(a4)) & a2(a3)))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3292 | unknown
h: exists a2.(exists a3.(varkenskotelet(a3) & a2(a3)) & exists z1316.(kok(z1316) & a2(z1316)))
p: exists a2.(exists a3.(wortel(a3) & a2(a3)) & exists z1317.(vrouw(z1317) & a2(z1317)))
s:False | False 
------------------------------
3322 | unknown
h: exists a2.(exists a3.(exists a4.(varkenskotelet(a4) & a3(a4)) & a2(a3)) & exists z1321.(vrouw(z1321) & a2(z1321)))
p: error
s: error
------------------------------
3338 | no
h: (\B.exists a4.(exists a5.(viool(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a5.(dak(a5) & op(a3,a5)) & B(a3)))(\B.exists a2.(man(a2) & B(a2)))
p: error
s: error
------------------------------
3364 | yes
h: \B.(exists a1.schoon(a1) & exists a3.(exists a4.(garnaal(a4) & a3(a4)) & vrouw(a3))(B))
p: \B.(exists a1.schoon(a1) & exists a3.(exists a4.(garnaal(a4) & a3(a4)) & exists z1336.(vrouw(z1336) & a3(z1336)))(B))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3373 | yes
h: error
p: (((\A B.A & B)(\B.exists a4.(waterscooter(a4) & B(a4))))(\A.A(\a2.rijden(a2))))(\B.exists a2.(vrouw(a2) & B(a2)))
s: error
------------------------------
3384 | yes
h: exists a2.(exists a3.(exists a5.((((\A B.A & B)(\B.exists a8.(pandabeer(a8) & B(a8))))(\A.A(\a6.eten(a6))))(a5) & bamboe(a5))(exists b.persoon(b)))(a3) & a2(a3) & exists a1.(entity(a1) & a2(a1)))
p: exists a2.(exists a3.bamboe(exists b.persoon(b),a3) & a2(a3) & exists z1338.(pandabeer(z1338) & a2(z1338)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((exists a3 (%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3398 | unknown
h: exists a4.(kom(a4) & in(\B.exists a3.(-exists a4.(ei(a4) & a3(a4)) & B(a3)),a4))(\a2.vrouw(a2))
p: exists a2.(exists a3.(ei(a3) & a2(a3)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3420 | unknown
h: exists a2.(exists a3.(man(a3) & a2(a3)) & exists z1348.(exists a3.groot(a3) & vis(z1348) & a2(z1348)))
p: exists a2.(exists a3.((((\A B.A & B)(\A B.exists a6.(A(a6) & B(a6))))(\a4.vis(a4)))(a3) & a2(a3)) & exists z1353.(vrouw(z1353) & a2(z1353)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3433 | yes
h: (\A B.A & B)(exists a3.(exists a4.(schaal(a4) & a3(a4)) & exists z1360.(persoon(z1360) & a3(z1360))))
p: \C.((((\A B.A & B)(\B.exists a5.(persoon(a5) & B(a5))))(\A.A(\a3.inboteren(a3))))(\B.exists a2.(dienblad(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3459 | unknown
h: (((\A B.A & B)(\B.exists a4.(bijl(a4) & B(a4))))(\B.exists a3.(exists a4.(houtblok(a4) & a3(a4)) & B(a3))))(\B.exists a2.(man(a2) & B(a2)))
p: error
s: error
------------------------------
3485 | unknown
h: (exists a3.(exists a6.(raam(\C.uit(a6,C)) & exists a5.(tafel(\C.op(a5,C)) & a6(a5)))(exists b.persoon(b)))(a3) & kat(a3))
p: (((\A B.A & B)(\a4.rek(a4)))(\B.exists a3.(raam(\C.uit(a3,C)) & tafel(\C.naar(\C.uit(a3,C),C)) & B(a3))))(\a2.kat(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (exists a3 (%%START ERROR%%exists a6.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3501 | yes
h: exists a2.(baby(a2) & hond(a2))
p: exists a2.(exists a3.(baby(a3) & a2(a3)) & exists z1378.(hond(z1378) & a2(z1378)))
s:False | False 
------------------------------
3505 | unknown
h: exists a2.(exists a3.(exists a5.(exists a6.(knoflook(a6) & exists a8.(stuk(a8) & \C.aan(a8,C) & in(a5,a8))) & \B.exists a4.(a5(a4) & B(a4)))(a3) & a2(a3)) & exists z1382.(vrouw(z1382) & a2(z1382)))
p: exists a1.(entity(a1) & exists a3.(knoflook(a3) & exists z1383.(vrouw(z1383) & a3(z1383)))(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 (%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3518 | unknown
h: exists a2.(vrouw(a2) & dansen(a2))
p: \B C.B(\D.-man(\a2.dansen(a2),\E.E(D),C))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3536 | yes
h: \C.(exists a5.(pan(a5) & in(\A.A(\a3.koken(a3)),a5))(\Q.exists a2.(okra(a2) & Q(a2))))(C)
p: exists z1392.(pan(z1392) & in(\B.exists a3.(exists z1391.(\B.(exists a4.z1391(exists b.persoon(b),a4) & B(a4)) & a3(z1391)) & B(a3)),z1392))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3586 | yes
h: exists a2.(trommel(\C.op(a2,C)) & exists z1411.(man(z1411) & a2(z1411)))
p: exists a2.(trommel(\C.op(a2,C)) & exists z1410.(man(z1410) & a2(z1410)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (trommel(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3598 | yes
h: exists a2.(exists a3.(oefening(a3) & a2(a3)) & exists z1414.(man(z1414) & a2(z1414)))
p: exists a2.(exists a3.(vloeroefening(a3) & a2(a3)) & exists z1415.(exists a3.eén(a3) & man(z1415) & a2(z1415)))
s: 'utf-8' codec can't decode byte 0xc3 in position 13826: invalid continuation byte
------------------------------
3625 | no
h: error
p: exists a4.(pan(a4) & in(\B.exists a3.(exists a4.(vlees(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(vrouw(a2) & B(a2)))
s: error
------------------------------
3626 | yes
h: \C.((((\A B.A & B)(\B.exists a5.(pan(a5) & B(a5))))(\A.A(\a3.doen(a3))))(\a2.vlees(a2)))(C)
p: \B.exists a1.((exists a4.(vlees(a4) & exists a5.(pan(a5) & in(a4,a5)))(\A B.(exists a2.A(exists b.persoon(b),a2) & B(a2))))(a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3657 | yes
h: (((\A B.A & B)(\B.exists a4.(jongen(a4) & B(a4))))(\B C.exists a4.(exists a6.(water(a6) & met(a4,a6)) & B(a4))(C)))(\B.exists a2.(kruik(a2) & B(a2)))
p: exists a3.(exists a4.(kruik(a4) & a3(a4)) & exists a4.(water(a4) & met(a3,a4)))(\B.exists a2.(jongen(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3661 | unknown
h: exists a3.(exists a4.(kruik(a4) & a3(a4)) & exists a4.(water(a4) & met(a3,a4)))(\B.exists a2.(jongen(a2) & B(a2)))
p: exists a3.(water(a3) & exists a4.((((\A B.A & B)(\B.exists a7.(mok(a7) & B(a7))))(\a5.kraan(a5)))(a4) & uit(a3,a4)))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3670 | yes
h: regen(\C.in(\A.A(\a2.lopen(a2)),C),\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(exists a4.(exists a5.(man(a5) & a4(a5)) & op(a2,a4)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    regen(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3680 | no
h: exists a2.(-exists a3.(exists a5.(exists a6.(exists a7.(circuit(a7) & a6(a7)) & a5(a6)) & racer(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: error
s: error
------------------------------
3711 | no
h: exists a2.(exists a3.(speelgoedwag(a3) & a2(a3)) & exists z1450.(speelgoedtrein(z1450) & a2(z1450)))
p: exists a2.(exists a3.(speelgoedwag(a3) & a2(a3)) & exists z1448.(speelgoedtrein(z1448) & a2(z1448)))
s:True | False 
------------------------------
3721 | yes
h: \C.((((\A B.A & B)(((\A B.A & B)(\Q.exists a8.(schijf(a8) & Q(a8))))(\a6.persoon(a6))))(\A.A(\a3.snijden(a3))))(\Q.exists a2.(ui(a2) & Q(a2))))(C)
p: \F1456.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B.exists a5.(exists a6.(ui(a6) & a5(a6)) & B(a5)),a6))))(\a3.persoon(a3)))(a1) & F1456(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3733 | yes
h: exists z1465.(\B.(exists a4.z1465(exists b.persoon(b),a4) & B(a4)) & in(\A.A(\a2.zwemmen(a2)),z1465))(\B.exists a2.(racer(a2) -> B(a2)))
p: exists z1464.(\B.(exists a4.z1464(exists b.persoon(b),a4) & B(a4)) & in(\A.A(\a2.racen(a2)),z1464))(\Q.exists a2.(zwemmer(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists z1465.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3747 | unknown
h: exists a2.(exists a3.(gitaar(a3) & a2(a3)) & exists z1468.(vrouw(z1468) & a2(z1468)))
p: exists a2.(gitaar(\C.op(a2,C)) & exists z1466.(exists a3.getalenteerd(a3) & man(z1466) & a2(z1466)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (gitaar(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3790 | yes
h: exists a2.(exists a3.(courgette(a3) & a2(a3)) & persoon(a2))
p: exists a2.(exists a3.(courgette(a3) & a2(a3)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (%%START ERROR%%exists a3 (courgette(a3) & a2(a3)) & \B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3812 | yes
h: exists a2.(exists a3.((((\A B.A & B)(\Q.exists a6.(reep(a6) & Q(a6))))(\B.(exists a5.groen(a5) & paprika(B))))(a3) & a2(a3)) & exists z1489.(vrouw(z1489) & a2(z1489)))
p: error
s: error
------------------------------
3855 | unknown
h: error
p: exists a3.(exists a4.(midden(a4) & a3(a4)) & exists a4.(weg(a4) & op(a3,a4)))(\B.exists a2.(man(a2) & B(a2)))
s: error
------------------------------
3861 | unknown
h: error
p: exists a4.(wandelpad(a4) & op(\F1508.exists a2.((((\A B.A & B)(\a5.wildernis(a5)))(\a3.man(a3)))(a2) & F1508(a2)),a4))
s: error
------------------------------
3862 | unknown
h: exists a3.(exists a4.(lui(a4) & a3(a4)) & exists a4.(weg(a4) & op(a3,a4)))(\B.exists a2.(man(a2) & B(a2)))
p: (((\A B.A & B)(\a4.wildernis(a4)))(((\A B.A & B)(\B.exists a5.(pad(a5) & B(a5))))(\A.A(\a3.lopen(a3)))))(\a2.man(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3880 | yes
h: exists a3.(exists a4.(ondersteboven(a4) & a3(a4)) & plafond(\C.op(a3,C)))(\a2.man(a2))
p: (((\A B.A & B)(\B.(plafond(B) & exists a7.(kamer(a7) & van(B,a7)))))(\A.A(\a2.dansen(a2))))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3897 | no
h: \B.exists a1.(exists a2.(man(a2) & a1(a2)) & B(a1))
p: exists a2.(-exists a3.((((\A B.A & B)(\A B.exists a6.(A(a6) & B(a6))))(\a4.man(a4)))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3909 | yes
h: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\A.A(\a3.bespelen(a3))))(\a2.gitaar(a2)))(C)
p: (\B.exists a4.(exists a5.(gitaar(a5) & a4(a5)) & B(a4)) & \A.A(\a2.zingen(a2)))(\a2.man(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3910 | unknown
h: (\B.exists a4.(exists a5.(gitaar(a5) & a4(a5)) & B(a4)) & \A.A(\a2.zingen(a2)))(\a2.man(a2))
p: (\A B.A & B)(exists a3.(gitaar(a3) & exists z1526.(man(z1526) & a3(z1526))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3922 | no
h: (bijzijn(\C.in(\A.A(\a2.dansen(a2)),C)) & exists a7.(mens(a7) -> van(\C.in(\A.A(\a2.dansen(a2)),C),a7)))(\Q.exists a2.(jongen(a2) & Q(a2)))
p: (bijzijn(\C.in(\B C.B(\D.-dansen(D,C)),C)) & exists a7.(mens(a7) -> van(\C.in(\B C.B(\D.-dansen(D,C)),C),a7)))(\Q.exists a2.(jongen(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (bijzijn(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3941 | no
h: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(kalender(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & jongen(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: exists a2.(exists a4.(kalender(a4) & naar(a2,a4)) & exists z1470.(jongen(z1470) & a2(z1470)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
3982 | unknown
h: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1554.(vrouw(z1554) & a2(z1554)))
p: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z534.(vrouw(z534) & a2(z534)))
s:True | False 
------------------------------
3996 | unknown
h: exists a2.(exists a3.(piano(a3) & a2(a3)) & exists z1556.(jongen(z1556) & a2(z1556)))
p: error
s: error
------------------------------
4001 | yes
h: exists a2.(exists a3.(touw(a3) & a2(a3)) & exists z1049.(man(z1049) & a2(z1049)))
p: exists a2.(exists a3.roekeloos(a3) & exists a4.(touw(a4) & a2(a4)) & exists z1558.(man(z1558) & a2(z1558)))
s:False | False 
------------------------------
4006 | yes
h: error
p: exists a2.(exists a3.(touw(a3) & a2(a3)) & exists z1049.(man(z1049) & a2(z1049)))
s: error
------------------------------
4011 | yes
h: ((\A B.A & B)(\B.exists a3.(exists a4.(touw(a4) & a3(a4)) & B(a3))))(\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(exists a3.(touw(a3) & a2(a3)) & exists z1049.(man(z1049) & a2(z1049)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    ((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4015 | yes
h: error
p: error
s: error
------------------------------
4031 | unknown
h: error
p: (((\A B.A & B)(\B.(exists a4.(hand(a4) & exists b.persoon(b)(a4)) & B(a4))))(\B.exists a3.(exists a4.(tegel(a4) & a3(a4)) & B(a3))))(\B.exists a2.(man(a2) & B(a2)))
s: error
------------------------------
4054 | yes
h: (((\A B.A & B)(\a4.weg(a4)))(\A.A(\a2.rennen(a2))))(\B.exists a2.(hond(a2) & B(a2)))
p: (((\A B.A & B)(\a4.weg(a4)))(\B.exists a3.(exists a4.(ademloos(a4) & a3(a4)) & B(a3))))(\B.exists a2.(hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4060 | unknown
h: (((\A B.A & B)(\a4.weg(a4)))(\B.exists a3.(exists a4.(ademloos(a4) & a3(a4)) & B(a3))))(\B.exists a2.(hond(a2) & B(a2)))
p: (((\A B.A & B)(\a4.weg(a4)))(\A.A(\a2.rennen(a2))))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4066 | yes
h: exists a3.(exists a4.(mes(a4) & a3(a4)) & exists a4.(boom(a4) & naar(a3,a4)))(\a2.man(a2))
p: exists a3.(exists a4.(mes(a4) & a3(a4)) & exists a4.(boom(a4) & naar(a3,a4)))(\a2.man(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4067 | unknown
h: exists a3.(exists a4.(mes(a4) & a3(a4)) & exists a4.(boom(a4) & naar(a3,a4)))(\a2.man(a2))
p: exists a3.(exists a4.(mes(a4) & a3(a4)) & exists a4.(boom(a4) & uit(a3,a4)))(\a2.man(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4079 | yes
h: (((\A B.A & B)(\B.exists a4.(paard(a4) & B(a4))))(\A.A(\a2.rijden(a2))))(\B.exists a2.(man(a2) & B(a2)))
p: (((\A B.A & B)(\B.exists a4.(paard(a4) & B(a4))))(\A.A(\a2.rijden(a2))))(\Q.exists a2.(exists a3.eén(a3) & man(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4086 | no
h: exists a2.(exists a3.(foto(a3) & a2(a3)) & exists z1582.(man(z1582) & a2(z1582)))
p: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(tekening(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4114 | no
h: exists a2.(exists a3.(pizza(a3) & a2(a3)) & exists z1585.(man(z1585) & a2(z1585)))
p: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(voedsel(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4135 | yes
h: (((\A B.A & B)(\B.exists a4.(trampoline(a4) & B(a4))))(\A.A(\a2.springen(a2))))(\B.exists a2.(hond(a2) & B(a2)))
p: (((\A B.A & B)(\B.exists a4.(trampoline(a4) & B(a4))))(\A.A(\a2.stuiteren(a2))))(\B.exists a2.(hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4140 | unknown
h: (((\A B.A & B)(\B.exists a4.(trampoline(a4) & B(a4))))(\B.exists a3.(exists a4.(exists a5.achterwaarts(a5) & salto(a4) & a3(a4)) & B(a3))))(\B.exists a2.(man(a2) & B(a2)))
p: (((\A B.A & B)(\B.exists a4.(trampoline(a4) & B(a4))))(\A.A(\a2.springen(a2))))(\Q.exists a2.(jongen(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4155 | no
h: exists a2.(-exists a3.((exists a5.((((\A B.A & B)(\B.exists a8.(exists a9.houten(a9) & fluit(a8) & B(a8))))(\A.A(\a6.spelen(a6))))(exists b.persoon(b)))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: exists a3.(exists a5.(houten(a5) & op(a3,a5)) & exists z1591.(man(z1591) & a3(z1591)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4157 | no
h: exists a2.(piano(\C.op(a2,C)) & exists z1599.(man(z1599) & a2(z1599)))
p: exists a2.(-exists a3.((exists a5.((((\A B.A & B)(\a8.piano(a8)))(\A.A(\a6.spelen(a6))))(exists b.persoon(b)))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (piano(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4164 | unknown
h: \F1602.exists a1.(((((\A B.A & B)(\A.A))(tekening(\B.bord(\C.op(B,C)))))(\a3.vrouw(a3)))(a1) & F1602(a1))
p: \F1601.exists a1.(((((\A B.A & B)(\A.A))(tekening(\B.bord(\C.op(B,C)))))(\a3.man(a3)))(a1) & F1601(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F1602.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4187 | no
h: (\A B.A & B)(exists a3.(exists a4.(pop(a4) & a3(a4)) & exists z1609.(hond(z1609) & a3(z1609))))
p: \B.exists a1.(exists a3.(-exists a4.(exists a6.(exists a7.exists a9.(exists a10.(stuk(a10) & speelgoed(a9)) & met(exists b.persoon(b),a9))(a7) & a6(a7) & hond(a6))(a4) & a3(a4)) & exists a2.(entity(a2) & a3(a2)))(a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4191 | unknown
h: exists a3.(exists a5.(stuk(a5) & met(a3,a5)) & exists z1610.(hond(z1610) & a3(z1610)))
p: (\A B.A & B)(exists a3.(exists a4.(pop(a4) & a3(a4)) & exists z1609.(hond(z1609) & a3(z1609))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4196 | unknown
h: \B.(exists a1.vurig(a1) & exists a3.(man(a3) & bidden(a3))(B))
p: exists a2.(man(a2) & dansen(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4288 | yes
h: exists a4.(stuk(a4) & in(\B.exists a3.(exists a4.(octopus(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(vrouw(a2) & B(a2)))
p: exists a4.(schijf(a4) & in(\B.exists a3.(exists a4.(exists a5.(octopus(a5) & a4(a5)) & a3(a4)) & B(a3)),a4))(\a2.vrouw(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4321 | no
h: \B.exists a1.(exists a2.(exists a4.(-exists a5.(man(a5) & a4(a5)) & exists a3.(entity(a3) & a4(a3)))(exists b.persoon(b)))(a2) & a1(a2) & B(a1))
p: exists a2.(man(a2) & tekenen(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4330 | no
h: \B.exists a1.(exists a2.(exists a4.(-exists a5.(man(a5) & a4(a5)) & exists a3.(entity(a3) & a4(a3)))(exists b.persoon(b)))(a2) & a1(a2) & B(a1))
p: man(\a1.tekenen(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4342 | yes
h: exists a2.(exists a3.(vrucht(a3) & a2(a3)) & exists z1655.(man(z1655) & a2(z1655)))
p: exists a2.(exists a3.(banaan(a3) & a2(a3)) & exists z1210.(man(z1210) & a2(z1210)))
s:False | False 
------------------------------
4360 | yes
h: exists a2.(exists a3.(papier(a3) & a2(a3)) & exists z1659.(man(z1659) & a2(z1659)))
p: exists a2.(exists a3.(brief(a3) & a2(a3)) & exists z1658.(man(z1658) & a2(z1658)))
s:False | False 
------------------------------
4376 | unknown
h: error
p: exists a2.(exists a4.(gitaar(a4) & op(a2,a4)) & exists z486.(man(z486) & a2(z486)))
s: error
------------------------------
4411 | unknown
h: exists a3.(exists a4.(mee(a4) & a3(a4)) & exists a4.(bandenrolwedstrijd(a4) & aan(a3,a4)))(\Q.exists a2.(exists a3.twee(a3) & man(a2) & Q(a2)))
p: exists a2.(exists a5.(exists a6.(\C.aan(a6,C) & a5(a6)) & band(a5) & exists a7.(tractor(a7) & van(a5,a7)))(a2) & exists z1679.((((\A B.A & B)(\B.exists a5.(race(a5) & B(a5))))(\B.(exists a4.twee(a4) & man(B))))(z1679) & a2(z1679)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4429 | unknown
h: \B.exists a1.(aan(\B.exists a3.((exists a4.oud(a4) & vrouw(a3)) -> B(a3)),a1) & B(a1))
p: \B.exists a1.(aan(\a3.man(a3),a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4477 | unknown
h: exists a2.(inhoud(a2) & exists a6.(\B.exists z1705.(a6(z1705) & B(z1705)) & van(a2,a6)) & exists z1706.(man(z1706) & a2(z1706)))
p: exists a2.(exists a3.(voetbal(a3) & a2(a3)) & exists z1703.(man(z1703) & a2(z1703)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((inhoud(a2) & exists a6 (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4505 | yes
h: exists a2.(patiënt(a2) & dokter(a2))
p: exists a2.(exists a3.(man(a3) & a2(a3)) & arts(a2))
s: 'utf-8' codec can't decode byte 0xc3 in position 589: invalid continuation byte
------------------------------
4520 | no
h: exists a2.(exists a4.(gitaar(a4) & op(a2,a4)) & exists z486.(man(z486) & a2(z486)))
p: exists a2.(-exists a3.((exists a5.((((\A B.A & B)(\B.exists a8.(gitaar(a8) & B(a8))))(\A.A(\a6.spelen(a6))))(exists b.persoon(b)))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4614 | no
h: exists a4.(auto(a4) & in(\A.A(\a2.rijden(a2)),a4))(\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(auto(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4638 | unknown
h: exists a2.(exists a3.(harp(a3) & a2(a3)) & exists z1355.(man(z1355) & a2(z1355)))
p: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\A.A(\a3.bespelen(a3))))(\B.exists a2.(keyboard(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4650 | no
h: (exists a3.exists a4.(exists a6.(exists a7.(exists a9.(zwaard(a9) & met(a7,a9)) & a6(a7)) & touw(a6))(a4) & exists b.persoon(b)(a4))(a3) & exists z1754.(-exists a4.(man(a4) & z1754(a4)) & a3(z1754)))(\A.exists a1.(entity(a1) & A(a1)))
p: exists a2.(exists a3.(exists a5.(((\A B.A & B)(\B.exists a8.(zwaard(a8) & met(B,a8))))(a5) & exists z1759.dik(z1759) & touw(a5))(a3) & a2(a3)) & exists z1762.(man(z1762) & a2(z1762)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4661 | yes
h: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & exists z1093.(vrouw(z1093) & a2(z1093)))
p: exists a4.(schijf(a4) & in(\B.exists a3.(exists a4.(aardappel(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4707 | unknown
h: (((\A B.A & B)(\a4.strand(a4)))(\A.A(\a2.voetballen(a2))))(\B.exists a2.(exists a3.(groep(a3) & jongen(a2)) & B(a2)))
p: (((\A B.A & B)(\a4.strand(a4)))(\A.A(\a2.voetballen(a2))))(\B.exists a2.(exists a3.(groep(a3) & man(a2)) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4734 | yes
h: exists a2.(exists a3.(exists a5.(((\A B.A & B)(\B.exists a8.(pistool(a8) & op(B,a8))))(a5) & geluiddemper(a5))(a3) & a2(a3)) & exists z1797.(man(z1797) & a2(z1797)))
p: (((\A B.A & B)(\B.exists a4.(pistool(a4) & B(a4))))(\B.exists a3.(exists a4.(geluiddemper(a4) & a3(a4)) & B(a3))))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 (%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4755 | unknown
h: (((\A B.A & B)(\B.exists a4.(strand(a4) & B(a4))))(\B.exists a3.(-exists a4.(exists a6.(exists a7.(exists a8.viool(exists b.persoon(b),a8) & a7(a8) & a6(a7)) & meisje(a6))(a4) & a3(a4)) & B(a3))))(\A.exists a1.(entity(a1) & A(a1)))
p: \B.exists a1.(((\B C.aan(B,C) & \B.exists a4.(bank(\C.op(a4,C)) & B(a4)))(\a3.meisje(a3)))(a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4767 | no
h: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(slang(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: exists a2.(exists a3.(slang(a3) & a2(a3)) & exists z1805.(man(z1805) & a2(z1805)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4776 | no
h: exists a2.(exists a3.(gitaar(a3) & a2(a3)) & exists z1812.(jongen(z1812) & a2(z1812)))
p: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(gitaar(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & jongen(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4803 | no
h: dierentuin(\C.in(\B.exists a3.(exists a4.(hond(a4) & a3(a4)) & B(a3)),C),\B.exists a2.(aap(a2) & B(a2)))
p: \F1828.exists a1.(((exists a4.exists a5.((((\A B.A & B)(\a8.dierentuin(a8)))(\a6.hond(a6)))(a5) & exists b.persoon(b)(a5))(a4) & exists z1827.(-exists a5.(aap(a5) & z1827(a5)) & a4(z1827)))(\A.exists a2.(entity(a2) & A(a2))))(a1) & F1828(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    dierentuin(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4814 | unknown
h: dierentuin(\C.in(\B.exists a3.(exists a4.(hond(a4) & a3(a4)) & B(a3)),C),\B.exists a2.(aap(a2) & B(a2)))
p: exists a2.(staart(\C.aan(a2,C)) & exists a7.(hond(a7) & van(\C.aan(a2,C),a7)) & exists z1830.(aap(z1830) & a2(z1830)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    dierentuin(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4816 | no
h: exists a2.(exists a3.gember(exists b.persoon(b),a3) & a2(a3) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
p: error
s: error
------------------------------
4823 | unknown
h: error
p: exists a2.(exists a3.gember(exists b.persoon(b),a3) & a2(a3) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
s: error
------------------------------
4831 | no
h: error
p: exists a2.(exists a3.(exists a5.(exists a8.(stuk(a8) & in(\A.A(\a6.door(a6)),a8))(a5) & aardappel(a5))(a3) & a2(a3)) & exists z1840.(man(z1840) & a2(z1840)))
s: error
------------------------------
4843 | no
h: exists a2.(-exists a3.((exists a5.exists a6.(exists a8.(exists a9.(exists a11.(mes(a11) & met(a9,a11)) & a8(a9)) & doos(a8))(a6) & exists b.persoon(b)(a6))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: exists a3.(exists a4.(doos(a4) & a3(a4)) & exists a4.(mes(a4) & met(a3,a4)))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4851 | yes
h: exists a2.(instrument(\C.op(a2,C)) & exists z1852.(band(z1852) & a2(z1852)))
p: \C.((((\A B.A & B)(\B.exists a5.(band(a5) & B(a5))))(\A.A(\a3.bespelen(a3))))(\B.exists a2.(instrument(a2) -> B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (instrument(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4852 | no
h: exists a2.(instrument(\C.op(a2,C)) & exists z1852.(band(z1852) & a2(z1852)))
p: \B C.B(\D.-(exists a3.(exists a4.(instrument(a4) -> a3(a4)) & exists z1853.(band(z1853) & a3(z1853)))(\E.E(D)))(C))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (instrument(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4866 | unknown
h: \F1854.exists a4.(aan(\B.exists a2.(vrouw(a2) & B(a2)),a4) & F1854(a4))
p: \F1369.exists a4.(aan(\B.exists a2.(persoon(a2) & B(a2)),a4) & F1369(a4))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F1854.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4891 | unknown
h: exists a3.(exists a4.(oefening(a4) & a3(a4)) & exists a4.(sportschool(a4) & in(a3,a4)))(\a2.man(a2))
p: exists a3.(man(a3) & doen(a3))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4916 | yes
h: (\B.exists a4.(exists a5.(muziekinstrument(a5) & a4(a5)) & B(a4)) & \A.A(\a2.zingen(a2)))(\B.exists a2.(man(a2) & B(a2)))
p: (\B.exists a4.(exists a6.(gitaar(a6) & op(a4,a6)) & B(a4)) & \A.A(\a2.zingen(a2)))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4934 | unknown
h: exists a2.(rekruut(\C.met(a2,C)) & exists z1868.(officier(z1868) & a2(z1868)))
p: exists a2.(exists a4.(officier(a4) & met(a2,a4)) & exists z1871.(rekruut(z1871) & a2(z1871)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (rekruut(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4963 | yes
h: exists a2.(exists a3.(exists a5.(exists a6.(knoflook(a6) & \C.aan(a5,C)) & \B.exists a4.(a5(a4) & B(a4)))(a3) & a2(a3)) & exists z1886.(vrouw(z1886) & a2(z1886)))
p: \C.((((\A B.A & B)(\B.exists a5.(vrouw(a5) & B(a5))))(\A.A(\a3.hakken(a3))))(\Q.exists a2.(knoflook(a2) & Q(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 (%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4966 | no
h: exists a2.(-exists a3.((exists a5.exists a7.((((\A B.A & B)(\A B.exists a10.(A(a10) & B(a10))))(\a8.vis(a8)))(a7) & exists b.persoon(b)(a7))(a5) & vrouw(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: \F1891.exists a1.(exists a3.(exists a4.((((\A B.A & B)(\A.A))(\a5.vis(a5)))(a4) & a3(a4)) & exists z1890.(vrouw(z1890) & a3(z1890)))(a1) & F1891(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
4983 | yes
h: \C.((((\A B.A & B)(\B.exists a5.(vrouw(a5) & B(a5))))(\A.A(\a3.berijden(a3))))(\B.exists a2.(paard(a2) & B(a2))))(C)
p: exists a2.(exists a4.(paard(a4) & op(a2,a4)) & exists z480.(vrouw(z480) & a2(z480)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5003 | yes
h: (\A B.A & B)((\F1912.exists a5.((\A B.A & B)(a5) & F1912(a5)) & \B.exists a4.(exists a5.(lade(a5) & a4(a5)) & B(a4)))(\B.exists a3.(kat(a3) & B(a3))))
p: (\A B.A & B)((\F1910.exists a5.((\A B.A & B)(a5) & F1910(a5)) & \B.exists a4.(exists a5.(exists a6.plastic(a6) & lade(a5) & exists a9.poot(exists b.persoon(b),a9) & met(a5,a9) & a4(a5)) & B(a4)))(\B.exists a3.(exists a4.groot(a4) & kat(a3) & B(a3))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5030 | yes
h: exists a2.(telefoon(\C.aan(a2,C)) & man(a2))
p: (((\A B.A & B)(\a4.telefoon(a4)))(\A.A(\a2.praten(a2))))(\a2.man(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (telefoon(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5047 | unknown
h: exists a2.(exists a3.(ui(a3) & a2(a3)) & exists z648.(vrouw(z648) & a2(z648)))
p: exists a2.(exists a3.(ui(a3) & a2(a3)) & exists z1930.(man(z1930) & a2(z1930)))
s:False | False 
------------------------------
5051 | no
h: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(deur(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: exists a2.(exists a3.(deur(a3) & a2(a3)) & exists z1933.(man(z1933) & a2(z1933)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5052 | unknown
h: exists a2.(exists a3.(ui(a3) & a2(a3)) & exists z1918.(man(z1918) & a2(z1918)))
p: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\A.A(\a3.openen(a3))))(\B.exists a2.(deur(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5082 | unknown
h: exists a2.(-exists a3.((exists a5.((((\A B.A & B)(\a8.piano(a8)))(\A.A(\a6.spelen(a6))))(exists b.persoon(b)))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: exists a2.(exists a3.(viool(a3) & a2(a3)) & exists z1950.(vrouw(z1950) & a2(z1950)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5110 | yes
h: exists a2.(exists a3.(maaltijd(a3) & a2(a3)) & exists z1963.(chef(z1963) & a2(z1963)))
p: exists a2.(exists a3 z1960.(exists b.persoon(b)(z1960) & a3(z1960)) & a2(a3) & exists z1961.(chefkok(z1961) & a2(z1961)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((exists a3 exists z1960 (%%START ERROR%%exists b.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5113 | yes
h: exists a2.(exists a3.twee(a3) & sumoworstelaar(a2) & vechten(a2))
p: \B.exists a1.(aan(\Q.exists a3.(exists a4.twee(a4) & sumoworstelaar(a3) & Q(a3)),a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5119 | unknown
h: water(\C.in(((\A B.A & B)(\B.exists a5.(waterspeel(a5) & B(a5))))(\A.A(\a3.rijden(a3))),C),\B.exists a2.(man(a2) & B(a2)))
p: \B.exists a1.(aan(\Q.exists a3.(exists a4.twee(a4) & sumoworstelaar(a3) & Q(a3)),a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    water(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5148 | unknown
h: (\A B.A & B)(exists a3.(exists a4.(exists a5.(stuk(a5) & brood(a4)) & a3(a4)) & exists z1983.(vrouw(z1983) & a3(z1983))))
p: (\A B.A & B)(exists a3.(exists a4.(exists a5.(stuk(a5) & brood(a4)) & a3(a4)) & exists z1981.(man(z1981) & a3(z1981))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5203 | yes
h: \C.((((\A B.A & B)(\B.exists a5.(vrouw(a5) & B(a5))))(\B.exists a4.(exists a6.(gerecht(a6) & in(a4,a6)) & B(a4))))(\Q.exists a2.(pasta(a2) & Q(a2))))(C)
p: exists a3.(pasta(a3) & exists a4.(gerecht(a4) & in(a3,a4)))(\a2.vrouw(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5206 | unknown
h: exists a2.(-exists a3.((((\A B.A & B)(\B.exists a6.(gerecht(a6) & B(a6))))(\a4.pasta(a4)))(a3) & a2(a3)) & vrouw(a2))
p: (((\A B.A & B)(\B.exists a4.(\B.exists z1998.(a4(z1998) & B(z1998)) & B(a4))))(\B.exists a3.(exists a4.(exists a5.kleverig(a5) & spul(exists b.persoon(b)))(a4) & a3(a4) & B(a3))))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5310 | no
h: exists a2.(a2(\z2042.spelen(z2042)) & exists z2043.(meisje(z2043) & a2(z2043)))
p: exists a2.(-exists a3.((exists a5.exists a6.(exists a7.(fluit(a7) & a6(a7)) & exists b.persoon(b)(a6))(a5) & meisje(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (a2(%%START ERROR%%\z2042.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5349 | yes
h: (((\A B.A & B)(\B.exists a4.(fluit(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\B.exists a2.(man(a2) & B(a2)))
p: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\A.A(\a3.bespelen(a3))))(\B.exists a2.(exists a3.groot(a3) & fluit(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5352 | no
h: exists a2.(-exists a3.((exists a5.exists a6.(exists a8.(fluit(a8) & op(a6,a8)) & exists b.persoon(b)(a6))(a5) & man(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: exists a2.(exists a4.(exists a5.groot(a5) & fluit(a4) & op(a2,a4)) & exists z2056.(man(z2056) & a2(z2056)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5374 | yes
h: \F2063.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B.exists a5.(exists a6.(octopus(a6) & a5(a6)) & B(a5)),a6))))(\B.exists a3.(vrouw(a3) & B(a3))))(a1) & F2063(a1))
p: \C.((((\A B.A & B)(\F2061.exists a5.((((\A B.A & B)(\Q.exists a8.(schijf(a8) & Q(a8))))(\a6.vrouw(a6)))(a5) & F2061(a5))))(\A.A(\a3.snijden(a3))))(\B.exists a2.(octopus(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F2063.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5454 | no
h: error
p: (((\A B.A & B)(\B.exists a4.(fluit(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\B.exists a2.(man(a2) & B(a2)))
s: error
------------------------------
5461 | unknown
h: (((\A B.A & B)(\B.exists a4.(fluit(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(fluit(\C.op(a2,C)) & exists z2091.(vrouw(z2091) & a2(z2091)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5498 | yes
h: exists a2.(exists a3.(fruit(a3) & a2(a3)) & exists z2106.(vrouw(z2106) & a2(z2106)))
p: exists a2.(exists a3.(citroen(a3) & a2(a3)) & exists z2105.(vrouw(z2105) & a2(z2105)))
s:False | False 
------------------------------
5540 | unknown
h: exists a2.(exists a3.(groep(a3) & mens(a2)) & marcheren(a2))
p: exists a4.(show(a4) & in(\A.A(\a2.dansen(a2)),a4))(\B.exists a2.(exists a3.(groep(a3) & mens(a2)) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5588 | yes
h: exists a2.(exists a3.(cupcake(a3) & a2(a3)) & exists z2133.(meisje(z2133) & a2(z2133)))
p: \C.((((\A B.A & B)(\B.exists a5.(meisje(a5) & B(a5))))(\A.A(\a3.eten(a3))))(\B.exists a2.(cupcake(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5657 | unknown
h: ((\A B.A & B)(\B.exists a3.(exists a4.(bed(a4) & a3(a4)) & B(a3))))(\B.exists a2.(persoon(a2) & B(a2)))
p: exists a4.(restaurant(a4) & in(\A.A(\a2.eten(a2)),a4))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    ((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5698 | unknown
h: (((\A B.A & B)(\a4.pizza(a4)))(\B.exists a3.(exists a4.(kaas(a4) & a3(a4)) & B(a3))))(\a2.man(a2))
p: exists a3.(pizza(a3) & exists a4.(kaas(a4) & met(a3,a4)))(\a2.kok(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5706 | unknown
h: ((\A B.A & B)(\B.exists a3.(exists a4.(jachtgeweer(a4) & a3(a4)) & B(a3))))(\B.exists a2.(man(a2) & B(a2)))
p: \B.exists a1.(exists a3.(exists a4.(jachtgeweer(a4) & \C.aan(a4,C) & a3(a4)) & exists z2171.(man(z2171) & a3(z2171)))(a1) & B(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    ((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5745 | unknown
h: exists a2.(exists a4.(pop(a4) & met(a2,a4)) & exists z2180.(baby(z2180) & a2(z2180)))
p: (((\A B.A & B)(\B.exists a4.(bal(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\B.exists a2.(tijgerwelp(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5747 | unknown
h: exists a2.(exists a4.(bal(a4) & met(a2,a4)) & exists z2182.(babytijger(z2182) & a2(z2182)))
p: exists a3.(exists a5.(stuk(a5) & met(a3,a5)) & exists z2181.(baby(z2181) & a3(z2181)))
s: (FATAL)
%%ERROR: The following symbols are used with multiple arities: met/1, met/2.


Fatal error:  The following symbols are used with multiple arities: met/1, met/2
------------------------------
5799 | yes
h: \C.((((\A B.A & B)(\B.exists a5.(persoon(a5) & B(a5))))(\A.A(\a3.schillen(a3))))(\B.exists a2.(aardappel(a2) & B(a2))))(C)
p: exists a2.(exists a3.(aardappel(a3) & a2(a3)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5806 | yes
h: exists a2.(exists a3.(boot(a3) & a2(a3)) & exists z2215.(man(z2215) & a2(z2215)))
p: exists a2.(exists a3.(kano(a3) & a2(a3)) & exists z2214.(man(z2214) & a2(z2214)))
s:False | False 
------------------------------
5904 | unknown
h: exists a4.(openluchtvoertuig(a4) & in(\B.exists a3.(weg(\C.op(a3,C)) & B(a3)),a4))((\B.exists a4.(vrouw(a4) & B(a4)) & \Q.exists a3.(man(a3) & Q(a3))))
p: error
s: error
------------------------------
5909 | unknown
h: (((\A B.A & B)(\A B.exists a4.(A(a4) & B(a4))))(\B.exists a3.(olie(a3) & B(a3))))(\a2.chef(a2))
p: exists a4.(kom(a4) & in(\B.exists a3.(exists a4.(ingrediënt(a4) & a3(a4)) & B(a3)),a4))(\B.exists a2.(vrouw(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5914 | yes
h: exists a2.(exists a4.(paard(a4) & op(a2,a4)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
p: \C.((((\A B.A & B)(\B.exists a5.(persoon(a5) & B(a5))))(\A.A(\a3.berijden(a3))))(\B.exists a2.(paard(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (%%START ERROR%%exists a4 (paard(a4) & op(a2,a4)) & \B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5920 | unknown
h: \F1859.exists a1.(((((\A B.A & B)(\A.A))(exists a6.(schijf(a6) & in(\B.exists a5.(exists a6.(aardappel(a6) & a5(a6)) & B(a5)),a6))))(\B.exists a3.(vrouw(a3) & B(a3))))(a1) & F1859(a1))
p: \C.((((\A B.A & B)(\B.exists a5.(persoon(a5) & B(a5))))(\A.A(\a3.berijden(a3))))(\B.exists a2.(paard(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F1859.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5924 | no
h: exists a2.(exists a3.(oefening(a3) & a2(a3)) & man(a2))
p: error
s: error
------------------------------
5930 | unknown
h: \B.exists a1.(aan(\Q.exists a3.(exists a4.twee(a4) & man(a3) & Q(a3)),a1) & B(a1))
p: error
s: error
------------------------------
5938 | yes
h: exists a4.(pot(a4) & in(\B.exists a3.(exists a4.(ingrediënt(a4) & a3(a4)) & B(a3)),a4))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: \C.((((\A B.A & B)(\B.exists a5.(man(a5) & B(a5))))(\B.exists a4.(exists a6.(pot(a6) & in(a4,a6)) & B(a4))))(\Q.exists a2.(groente(a2) & Q(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
5955 | unknown
h: (((\A B.A & B)(\A.A))(\B.exists a4.(exists a5.(bal(a5) & a4(a5)) & B(a4))))(\B.exists a3.(hond(a3) & B(a3)))
p: exists a3.(exists a4.(exists a6.(in(\A.A(\a7.achter(a7)),a6) & bal(a6))(a4) & a3(a4)) & exists z2254.(hond(z2254) & a3(z2254)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6001 | unknown
h: exists a2.(water(\C.in(a2,C)) & exists z2272.((((\A B.A & B)(\Q.exists a5.(exists a6.gouden(a6) & vacht(a5) & Q(a5))))(\a3.hond(a3)))(z2272) & a2(z2272)))
p: exists a2.(-exists a3.((((\A B.A & B)(\a6.water(a6)))(\B.(exists a5.bruin(a5) & hond(B))))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (water(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6005 | unknown
h: (((\A B.A & B)(\a4.stoep(a4)))((\A.A(\a4.lopen(a4)) & \B.exists a4.(exists a5.(exists a7.(a7(\z2288.omhoog(z2288)) & exists z2289.blauw(z2289) & shirt(a7))(a5) & a4(a5)) & B(a4)))))(\F2287.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.roze(a6) & bord(a5) & B(a5))))(\B.(exists a4.jong(a4) & meisje(B))))(a2) & F2287(a2)))
p: \F2286.(exists a1.vast(a1) & ((\B.exists a5.(exists a6.(exists a7.roze(a7) & bord(a6) & a5(a6)) & B(a5)) & ((\A B.A & B)(\a6.stoep(a6)))(\A.A(\a4.lopen(a4))))(\F2285.exists a3.(exists a4.jong(a4) & (((\A B.A & B)(\B.exists a7.(exists a8.blauw(a8) & shirt(a7) & B(a7))))(\a5.meisje(a5)))(a3) & F2285(a3))))(F2286))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6042 | unknown
h: water(\C.in(\A.A(\a2.spetteren(a2)),C),\B.exists a2.(exists a3.jong(a3) & kind(a2) & B(a2)))
p: (\F2303 C.((((\A B.A & B)(\B.exists a7.(exists a8.ander(a8) & persoon(a7) & B(a7))))(\A.A(\a5.begeleiden(a5))))(F2303))(C) & \B.exists a3.(water(\C.door(a3,C)) & B(a3)))(\B.(exists a3.klein(a3) & kind(B)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    water(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6047 | yes
h: error
p: error
s: error
------------------------------
6078 | unknown
h: exists a2.(zadel(\C.op(a2,C)) & exists a7.(paard(a7) & van(\C.op(a2,C),a7)) & exists z2326.((((\A B.A & B)(\B.exists a5.(spijkerbroek(a5) & B(a5))))(\a3.vrouw(a3)))(z2326) & a2(z2326)))
p: \F2332.exists a1.((exists a3.(exists a6.(exists a7.vrolijk(a7) & ((\A B.A & B)(\B.exists a10.(paardenzadel(a10) & op(B,a10))))(a6) & exists a5.(exists z2330.(spijkerbroek(z2330) & a5(z2330)) & a6(a5)))(exists b.persoon(b)))(a3) & persoon(a3))(a1) & F2332(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((zadel(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6119 | unknown
h: \B.exists a1.((exists a4.(exists z2353.(honkbal(z2353) & a4(z2353)) & exists a5.(bek(a5) & exists b.persoon(b)(a5)) & uit(a4,a5))(\B.exists a3.(exists a4.zwartwit(a4) & hond(a3) & B(a3))))(a1) & B(a1))
p: (exists a4.(bek(a4) & exists b.persoon(b)(a4)) & in(\B.exists a3.(exists a4.(honkbal(a4) & a3(a4)) & B(a3)),a4))((\Q.exists a4.(exists a5.wit(a5) & hond(a4) & Q(a4)) & \B.exists a3.(bruin(a3) & B(a3))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6131 | unknown
h: error
p: error
s: error
------------------------------
6146 | no
h: (\B.exists a4.(zonsondergang(\C.naar(a4,C)) & B(a4)) & \B.exists a3.(oceaan(\C.in(a3,C)) & B(a3)))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: (\B.exists a4.(zonsondergang(a4) & B(a4)) & \B.exists a3.(oceaan(\C.in(a3,C)) & B(a3)))(\Q.exists a2.(exists a3.twee(a3) & mens(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6153 | unknown
h: (\B.B(\a4.bewegingsloos(a4)) & \B.exists a3.(a3(\z2368.zitten(z2368)) & B(a3)))(\B.exists a2.(autocoureur(a2) & B(a2)))
p: error
s: error
------------------------------
6158 | unknown
h: exists a2.(exists a3.(exists a4.kleurrijk(a4) & helm(a3) & a2(a3)) & (((\A B.A & B)(\B.(exists a6.blauw(a6) & jas(B))))(\a3.persoon(a3)))(a2))
p: error
s: error
------------------------------
6203 | unknown
h: \C.((((\A B.A & B)(\B.(hoofd(B) & exists a8.(exists a9.(groep(a9) & mens(a8)) & van(B,a8)))))(\B.exists a4.(fiets(\C.met(a4,C)) & B(a4))))(\B.exists a2.(fietser(a2) & B(a2))))(C)
p: exists a2.(exists a3.((((\A B.A & B)(\B.(exists a6.(hoofd(exists b.persoon(b)) & exists a9.(exists a10.(groep(a10) & mens(a9)) & in(exists b.persoon(b),a9)))(a6) & B(a6))))(\a4.fiets(a4)))(a3) & a2(a3)) & exists z2398.(fietser(z2398) & a2(z2398)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6213 | unknown
h: (buurt(\C.in(\B.exists a3.(exists a5.(boot(a5) & zonsondergang(\C.voor(a5,C)) & op(a3,a5)) & B(a3)),C)) & exists a7.(vlag(a7) & van(\C.in(\B.exists a3.(exists a5.(boot(a5) & zonsondergang(\C.voor(a5,C)) & op(a3,a5)) & B(a3)),C),a7)))(\B.exists a2.(man(a2) & B(a2)))
p: error
s: error
------------------------------
6219 | yes
h: exists a2.(exists a4.(boot(a4) & zonsondergang(\C.voor(a4,C)) & op(a2,a4)) & exists z2407.(man(z2407) & a2(z2407)))
p: (buurt(\C.in(\B.exists a3.(exists a5.(boot(a5) & zonsondergang(\C.voor(a5,C)) & op(a3,a5)) & B(a3)),C)) & exists a7.(vlag(a7) & van(\C.in(\B.exists a3.(exists a5.(boot(a5) & zonsondergang(\C.voor(a5,C)) & op(a3,a5)) & B(a3)),C),a7)))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a4 ((boot(a4) & zonsondergang(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6228 | unknown
h: error
p: error
s: error
------------------------------
6231 | unknown
h: error
p: (((\A B.A & B)(\a4.gras(a4)))(exists a3.(entity(a3) & a3(\z2409.spelen(z2409)))))(\Q.exists a2.(exists a3.twee(a3) & hond(a2) & Q(a2)))
s: error
------------------------------
6280 | yes
h: gras(\C.in(\A.A(\a2.lopen(a2)),C),\B.exists a2.(exists a3.zwart(a3) & hond(a2) & B(a2)))
p: gras(\C.in((exists a5.zwart(exists b.persoon(b),a5) & lopen(a5)),C),\B.exists a3.(hond(a3) & B(a3)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    gras(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6287 | yes
h: gras(\C.in(\A.A(\a2.lopen(a2)),C),\B.exists a2.(exists a3.zwart(a3) & hond(a2) & B(a2)))
p: error
s: error
------------------------------
6315 | yes
h: (((\A B.A & B)(\B.exists a4.(exists a5.zonnig(a5) & dag(a4) & B(a4))))(((\A B.A & B)(\Q.exists a5.(exists a6.wit(a6) & sneeuw(a5) & Q(a5))))(\A.A(\a3.rennen(a3)))))(\B.exists a2.(exists a3.geel(a3) & hond(a2) & B(a2)))
p: (((\A B.A & B)(\B.exists a4.((exists a6.(entity(a6) & \B.(exists z2459.zonnig(z2459) & a6(B)))(\a5.dag(a5)))(a4) & B(a4))))(((\A B.A & B)(\Q.exists a5.(exists a6.wit(a6) & sneeuw(a5) & Q(a5))))(\A.A(\a3.lopen(a3)))))(\B.exists a2.(exists a3.geel(a3) & hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6330 | unknown
h: woestijn(\C.in(((\A B.A & B)(\B.exists a5.(boom(a5) & B(a5))))(\A.A(\a3.rennen(a3))),C),\F2462.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.roze(a6) & hemd(a5) & B(a5))))(\B.(exists a4.klein(a4) & jongen(B))))(a2) & F2462(a2)))
p: (\A.A(\a3.rennen(a3)) & \B.exists a3.((\B.exists a6.(exists a7.roze(a7) & hemd(a6) & B(a6)) & \B.exists a5.(spijkerbroek(a5) & B(a5)))(a3) & B(a3)))(\B.exists a2.(meisje(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    woestijn(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6344 | unknown
h: error
p: error
s: error
------------------------------
6358 | no
h: error
p: (\B.exists a4.(exists a5.(instrument(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a5.(exists a6.(baksteen(a6) & muur(a5)) & tegen(a3,a5)) & B(a3)))(((\A B.A & B)(\B.exists a5.(exists a6.rood(a6) & kostuum(a5) & B(a5))))(\a3.vrouw(a3)))
s: error
------------------------------
6394 | unknown
h: (((\A B.A & B)(\B.exists a4.(exists a5.prachtig(a5) & waterval(a4) & B(a4))))(((\A B.A & B)(\a5.weg(a5)))(\A.A(\a3.lopen(a3)))))(\a2.mens(a2))
p: exists a4.(exists a5.ondiep(a5) & bassin(a4) & in(\A.A(\a2.stromen(a2)),a4))(\B.exists a2.(waterval(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6396 | unknown
h: (((\A B.A & B)(\B.exists a4.(exists a5.stoffig(a5) & boerderij(a4) & B(a4))))(\B.exists a3.(exists a4.(exists a5.(roedel(a5) & exists a6.wit(a6) & schaap(a4)) & a3(a4)) & B(a3))))(\B.exists a2.(hond(a2) & B(a2)))
p: (((\A B.A & B)(\B.exists a4.(exists a5.stoffig(a5) & boerderij(a4) & B(a4))))(\B.exists a3.(exists a4.(exists a5.(roedel(a5) & exists a6.wit(a6) & schaap(a4)) & a3(a4)) & B(a3))))(\B.exists a2.(hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6450 | unknown
h: (\B.exists a4.(exists a5.(topje(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a5.(exists a6.geel(a6) & tank(a5) & in(a3,a5)) & B(a3)))(\B.exists a2.(exists a3.lachend(a3) & jongen(a2) & B(a2)))
p: (\A.A(\a3.lachen(a3)) & \B.exists a3.(exists a4.(exists a5.geel(a5) & tanktop(a4) & a3(a4)) & B(a3)))(\B.exists a2.(exists a3.klein(a3) & jongen(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6482 | unknown
h: exists a2.(exists a4.(exists a5.(veld(a5) & exists a8.(gletsjerijs(a8) & van(a5,a8)) & a4(a5)) & in(a2,a4)) & exists z2509.(persoon(z2509) & a2(z2509)))
p: error
s: error
------------------------------
6544 | no
h: error
p: (\B.exists a4.(doel(a4) & B(a4)) & \B.exists a3.(exists a4.(exists a5.geel(a5) & trui(a4) & a3(a4)) & B(a3)))(\a2.ijshockeykeeper(a2))
s: error
------------------------------
6568 | unknown
h: error
p: (((\A B.A & B)(\B.exists a4.(parkeerplaats(a4) & B(a4))))(((\A B.A & B)(\B.exists a5.(fiets(a5) & B(a5))))((\A.A(\a5.rijden(a5)) & \B.exists a5.(exists a6.(exists a7.blauw(a7) & helm(a6) & a5(a6)) & B(a5))))))(\B.exists a2.(vrouw(a2) & B(a2)))
s: error
------------------------------
6590 | unknown
h: exists a2.(exists a3.jong(a3) & vrouw(a2) & dansen(a2))
p: exists a2.(exists a4.één(a4) & been(\C.op(a2,C)) & exists z2557.(exists a3.jong(a3) & meisje(z2557) & a2(z2557)))
s: 'utf-8' codec can't decode byte 0xc3 in position 13738: invalid continuation byte
------------------------------
6592 | unknown
h: exists a2.(exists a3.jong(a3) & meisje(a2) & dansen(a2))
p: exists a2.(exists a4.één(a4) & been(\C.op(a2,C)) & exists z2557.(exists a3.jong(a3) & meisje(z2557) & a2(z2557)))
s: 'utf-8' codec can't decode byte 0xc3 in position 13739: invalid continuation byte
------------------------------
6598 | unknown
h: error
p: error
s: error
------------------------------
6625 | unknown
h: (((\A B.A & B)(\a4.borstel(a4)))(\A.A(\a2.lopen(a2))))(\B.exists a2.(exists a3.bruingeel(a3) & hond(a2) & B(a2)))
p: \F2581.exists a1.(exists a3.(-exists a4.((exists a6.exists a7.(exists a8.(veld(a8) & a7(a8)) & exists b.persoon(b)(a7))(a6) & (((\A B.A & B)(\Q.exists a8.(exists a9.beige(a9) & vlek(a8) & Q(a8))))(\B.(exists a7.wit(a7) & hond(B))))(a6))(a4) & a3(a4)) & exists a2.(entity(a2) & a3(a2)))(a1) & F2581(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6634 | yes
h: (\B.(exists a3.(ruiter(exists b.persoon(b)) & exists a5.(exists a7.(hindernis(a7) & over(a5,a7)) & exists b.persoon(b)(a5)))(a3) & B(a3)) & \B.exists a2.(paard(a2) & B(a2)))
p: error
s: error
------------------------------
6649 | yes
h: (((\A B.A & B)(\B.exists a4.(evenement(a4) & B(a4))))(\B.exists a3.(exists a4.(exists a5.mooi(a5) & jurk(a4) & a3(a4)) & B(a3))))(\Q.exists a2.((((\A B.A & B)(\B.(exists a5.(tienerjaar(a5) & exists b.persoon(b)(a5)) & B(a5))))(\B.(exists a4.twee(a4) & meisje(B))))(a2) & Q(a2)))
p: (((\A B.A & B)(\B.exists a4.(evenement(a4) & B(a4))))(\B.exists a3.(exists a4.(exists a5.mooi(a5) & jurk(a4) & a3(a4)) & B(a3))))(\Q.exists a2.(exists a3.twee(a3) & tienermeisje(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6673 | unknown
h: error
p: error
s: error
------------------------------
6705 | yes
h: error
p: error
s: error
------------------------------
6709 | unknown
h: error
p: exists a2.(exists a3.(exists a4.betonnen(a4) & trap(a3) & a2(a3)) & exists z2631.((((\A B.A & B)(\B.exists a5.(exists a6.roze(a6) & trui(a5) & B(a5))))(\B.(exists a4.klein(a4) & kind(B))))(z2631) & a2(z2631)))
s: error
------------------------------
6729 | unknown
h: \C.((((\A B.A & B)(\B.exists a5.(kind(a5) & B(a5))))(\A.A(\a3.maken(a3))))(\B.exists a2.(sneeuwbal(a2) & B(a2))))(C)
p: error
s: error
------------------------------
6740 | unknown
h: exists a2.(exists a4.((((\A B.A & B)(\a7.palmboom(a7)))(\a5.bank(a5)))(a4) & op(a2,a4)) & exists z2648.(exists a3.drie(a3) & mens(z2648) & a2(z2648)))
p: error
s: error
------------------------------
6756 | yes
h: exists a2.(exists a4.(exists a5.rotsachtig(a5) & ondergrond(a4) & op(a2,a4)) & (\B.exists a4.(exists a5.klein(a5) & exists a6.grijs(a6) & hond(a4) & B(a4)) & \B.exists a3.(exists a4.fors(a4) & exists a5.bruin(a5) & hond(a3) & B(a3)))(a2))
p: exists a2.(exists a4.(exists a5.rotsachtig(a5) & ondergrond(a4) & op(a2,a4)) & (\B.exists a4.(exists a5.klein(a5) & exists a6.grijs(a6) & hond(a4) & B(a4)) & \B.exists a3.(exists a4.groot(a4) & exists a5.bruin(a5) & hond(a3) & B(a3)))(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a4 ((exists a5 rotsachtig(a5) & ondergrond(a4)) & op(a2,a4)) & (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6764 | unknown
h: (((\A B.A & B)(\B.exists a4.(rivier(a4) & B(a4))))(((\A B.A & B)(\Q.exists a5.(rots(a5) & Q(a5))))(\A.A(\a3.lopen(a3)))))(\Q.exists a2.(exists a3.drie(a3) & jongen(a2) & Q(a2)))
p: (((\A B.A & B)(\B.exists a4.(rivier(a4) & B(a4))))(((\A B.A & B)(\Q.exists a5.(rots(a5) & Q(a5))))(\A.A(\a3.rusten(a3)))))(\Q.exists a2.(exists a3.drie(a3) & jongen(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6784 | no
h: error
p: (exists a5.zwart(a5) & kleden(\C.in(\B.exists a3.(-exists a4.(man(a4) & a3(a4)) & B(a3)),C)) & exists a8.(exists a9.(exists a10.zwart(a10) & masker(a9) & a8(a9)) & met(\C.in(\B.exists a3.(-exists a4.(man(a4) & a3(a4)) & B(a3)),C),a8)))(\A.exists a1.(entity(a1) & A(a1)))
s: error
------------------------------
6849 | unknown
h: error
p: error
s: error
------------------------------
6866 | unknown
h: exists a2.(-exists a3.((exists a5.((((\A B.A & B)(\B.(exists a8.hoog(a8) & exists a9.groen(a9) & gras(B))))(\A.A(\a6.rennen(a6))))(exists b.persoon(b)))(a5) & exists z2701.bruin(z2701) & hond(a5))(a3) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
p: (((\A B.A & B)(\F2693.exists a4.((((\A B.A & B)(\Q.exists a7.(exists a8.hoog(a8) & gras(a7) & Q(a7))))(\a5.veld(a5)))(a4) & F2693(a4))))(\A.A(\a2.rennen(a2))))(\B.exists a2.(exists a3.gouden(a3) & hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (-(exists a3 ((%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6912 | unknown
h: (((\A B.A & B)((\Q.exists a6.(\B.exists z2727.(a6(z2727) & B(z2727)) & Q(a6)) & \Q.exists a9.(\B.exists z2726.(a9(z2726) & B(z2726)) & Q(a9)) & \B.exists a8.(exists a9.wit(a9) & pet(a8) & B(a8)) & \B.exists a6.(exists a7.wit(a7) & vest(a6) & B(a6)))))(\B.exists a3.(exists a4.(exists a5.blauw(a5) & shirt(a4) & a3(a4)) & B(a3))))(\B.exists a2.(vrouw(a2) & B(a2)))
p: error
s: error
------------------------------
6932 | yes
h: (((\A B.A & B)(\B.exists a4.(board(a4) & B(a4))))(\B.exists a3.(lucht(\C.in(a3,C)) & B(a3))))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: exists a3.(exists a4.((((\A B.A & B)(\B.exists a7.(berg(a7) & B(a7))))(\a5.salto(a5)))(a4) & a3(a4)) & snowboarder(a3))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6955 | unknown
h: error
p: exists a2.(exists a4.(schommel(a4) & op(a2,a4)) & exists z2754.((((\A B.A & B)(\a5.groen(a5)))(\B.(exists a4.blond(a4) & jongen(B))))(z2754) & a2(z2754)))
s: error
------------------------------
6961 | unknown
h: (((\A B.A & B)(\a4.podium(a4)))(\B.exists a3.(exists a4.(gitaar(a4) & a3(a4)) & B(a3))))(\F2761.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.wit(a6) & hoed(a5) & B(a5))))(\a3.man(a3)))(a2) & F2761(a2)))
p: exists a2.((\B.exists a5.(exists a6.(gitaar(a6) & a5(a6)) & B(a5)) & \B.exists a4.(hoed(a4) & B(a4)))(a2) & exists z2764.(exists a3.blank(a3) & man(z2764) & a2(z2764)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
6971 | no
h: exists a4.(crossmotorrace(a4) & in(\B.exists a3.(exists a4.(sprong(a4) & a3(a4)) & B(a3)),a4))(\F2766.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.rood(a6) & uniform(a5) & B(a5))))(\a3.man(a3)))(a2) & F2766(a2)))
p: error
s: error
------------------------------
7002 | unknown
h: \C.((((\A B.A & B)(\B.(exists a5.(tegenstander(a5) & exists b.persoon(b)(a5)) & B(a5))))(\A.A(\a3.tackelen(a3))))(\B.exists a2.(voetballer(a2) & B(a2))))(C)
p: \C.exists a2.(rugbyspelers(a2) & -exists a3.(exists z2778.(\B.(exists a4.z2778(exists b.persoon(b),a4) & B(a4)) & a3(z2778)) & a3(a2))(C))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7007 | unknown
h: exists a2.(exists a4.(exists a5.(geval(a5) & blad(a4)) & op(a2,a4)) & exists z2782.(exists a3.wit(a3) & hond(z2782) & a2(z2782)))
p: exists a2.(exists a4.(exists a5.(geval(a5) & blad(a4)) & op(a2,a4)) & exists z2781.(exists a3.wit(a3) & hond(z2781) & a2(z2781)))
s:True | False 
------------------------------
7018 | yes
h: exists a2.(exists a4.(exists a5.uitgestrekt(a5) & arm(a4) & met(a2,a4)) & exists z2785.((((\A B.A & B)(\Q.exists a5.(exists a6.lichtgekleurd(a6) & kleding(a5) & Q(a5))))(\a3.kind(a3)))(z2785) & a2(z2785)))
p: error
s: error
------------------------------
7027 | unknown
h: (\A B.A & B)(exists a3.(gymrek(\C.op(a3,C)) & (\a5.meisje(a5) & \a4.jongen(a4))(a3)))
p: error
s: error
------------------------------
7043 | unknown
h: error
p: exists a2.(a2(\z2790.naakt(z2790)) & motorcrossrijder(a2))
s: error
------------------------------
7044 | unknown
h: error
p: error
s: error
------------------------------
7064 | yes
h: error
p: (((\A B.A & B)(\B.exists a4.(helling(a4) & B(a4))))(\F2805 C.((((\A B.A & B)(\B.exists a6.(rolschaatser(a6) & B(a6))))(\A.A(\a4.uitvoeren(a4))))(F2805))(C)))(\B.exists a2.(truc(a2) & B(a2)))
s: error
------------------------------
7088 | unknown
h: exists a2.(exists a4.(voetbalwedstrijd(a4) & naar(a2,a4)) & menigte(a2))
p: exists a2.(veld(\C.in(\A.A(\a3.stil(a3)),C),a2) & exists z2820.(exists a3.(groep(a3) & voetballer(z2820)) & a2(z2820)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (veld(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7093 | yes
h: (\B.exists a4.(camera(\C.naar(a4,C)) & B(a4)) & \B.exists a3.(a3(\z2822.samen(z2822)) & B(a3)))(\B.exists a2.(exists a3.(groep(a3) & mens(a2)) & B(a2)))
p: (\B.exists a4.(camera(\C.naar(a4,C)) & B(a4)) & \B.exists a3.(a3(\z2821.samen(z2821)) & B(a3)))(\B.exists a3.(groep(a3) & mens(B)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7214 | no
h: (exists a4.(mond(a4) & exists b.persoon(b)(a4)) & in(\F2891.exists a3.(-exists a4.((exists a6.((((\A B.A & B)(\a9.tuin(a9)))(\B.exists a8.(exists a10.(exists a11.(stuk(a11) & speelgoed(a10)) & met(a8,a10)) & B(a8))))(exists b.persoon(b)))(a6) & exists z2889.bruin(z2889) & hond(a6))(a4) & a3(a4)) & F2891(a3)),a4))(\A.exists a1.(entity(a1) & A(a1)))
p: error
s: error
------------------------------
7228 | unknown
h: exists a2.(exists a3.hoog(a3) & gras(\C.over(a2,C)) & exists z2896.((((\A B.A & B)(\B.exists a5.(exists a6.groen(a6) & shirt(a5) & B(a5))))(\a3.persoon(a3)))(z2896) & a2(z2896)))
p: exists a2.((\Q.exists a5.(exists z2902.(arm(z2902) & a5(z2902)) & Q(a5)) & \F2901.-exists a4.((exists a6.((((\A B.A & B)(\a9.lucht(a9)))(\B.exists a8.(exists a10.(exists a11.(knie(a11) & a10(a11)) & met(a8,a10)) & B(a8))))(exists b.persoon(b)))(a6) & jongen(a6))(a4) & F2901(a4)))(a2) & exists a1.(entity(a1) & a2(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((exists a3 hoog(a3) & gras(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7311 | yes
h: (\B.exists a4.(exists a5.(sigaret(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a4.(strohoed(a4) & a3(a4)) & B(a3)))(\B.exists a2.(man(a2) & B(a2)))
p: \C.((((\A B.A & B)(\B.(man(B) & strohoed(\C.met(B,C)))))(\A.A(\a3.roken(a3))))(\B.exists a2.(sigaret(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7319 | unknown
h: (straat(\C.in(\B.exists a5.(exists a7.(eenwieler(a7) & op(a5,a7)) & B(a5)),C)) & \B.exists a3.(exists a4.(exists a5.blauw(a5) & exists a6.(geruit(a6) & hemd(a4)) & a3(a4)) & B(a3)))(\B.exists a2.(man(a2) & B(a2)))
p: error
s: error
------------------------------
7356 | unknown
h: (((\A B.A & B)(\B.exists a4.(standbeeld(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\Q.exists a2.(exists a3.twee(a3) & kind(a2) & Q(a2)))
p: exists a4.(park(a4) & in(\B.exists a3.(exists a4.(standbeeld(a4) & a3(a4)) & B(a3)),a4))(\Q.exists a2.(exists a3.klein(a3) & kind(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7363 | unknown
h: (((\A B.A & B)(\B.exists a4.(stad(a4) & B(a4))))(\B.exists a3.(uitzicht(\C.naar(a3,C)) & B(a3))))(\B.exists a2.(vrouw(a2) & B(a2)))
p: \C.((((\A B.A & B)(\B.exists a5.(exists a6.blond(a6) & dame(a5) & B(a5))))(\A.A(\a3.bekijken(a3))))(\B.exists a2.(toren(a2) & B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7374 | unknown
h: exists a2.(exists a4.(bergtop(a4) & op(a2,a4)) & \B.(exists a1.a2(exists b.persoon(b),a1) & B(a1)))
p: exists a1.(entity(a1) & exists a3.((((\A B.A & B)(\Q.exists a8.(wolk(a8) & Q(a8))))(\B.(top(B) & rots(\C.van(B,C)))))(\C.op(a3,C)) & exists z2961.(man(z2961) & a3(z2961)))(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (%%START ERROR%%exists a4 (bergtop(a4) & op(a2,a4)) & \B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7394 | unknown
h: exists a4.(zwembad(a4) & in(\B.exists a3.(exists a5.(water(a5) & onder(a3,a5)) & B(a3)),a4))(\B.exists a2.(kind(a2) & B(a2)))
p: (((\A B.A & B)(\Q.exists a4.(water(a4) & Q(a4))))((\A.A(\a4.zwemmen(a4)) & \B.exists a4.(camera(\C.naar(a4,C)) & B(a4)))))(\B.exists a2.(kind(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7410 | unknown
h: exists a2.(exists a3.(exists a4.zwart(a4) & armband(a3) & a2(a3)) & exists z2980.(voetballer(z2980) & a2(z2980)))
p: exists a2.(exists a4.roodwit(a4) & tenue(a2) & exists z2978.(exists a3.amerikaans(a3) & voetballer(z2978) & a2(z2978)))
s:False | False 
------------------------------
7445 | yes
h: error
p: exists a2.(\F2996.(exists a3.achter(a2,exists b.persoon(b),a3) & F2996(a3)) & (\a4.vrouw(a4) & \B.exists a3.(exists a5.klein(a5) & meisje(a3) & B(a3)))(a2))
s: error
------------------------------
7448 | unknown
h: error
p: park(\C.in(((\A B.A & B)(\B.exists a5.(schommel(a5) & B(a5))))(\B.exists a4.(exists a5.(opwinding(a5) & a4(a5)) & B(a4))),C),\B.exists a2.(exists a3.klein(a3) & kind(a2) & B(a2)))
s: error
------------------------------
7464 | unknown
h: water(\C.in(\B.exists a3.(exists a5.(surfplank(a5) & van(a3,a5)) & B(a3)),C),\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(golf(\C.op(a2,C)) & exists z2383.(surfer(z2383) & a2(z2383)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    water(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7466 | yes
h: error
p: exists a2.(exists a4.(exists a5.slecht(a5) & exists a6.verlicht(a6) & kamer(a4) & in(a2,a4)) & exists a3.(groep(a3) & mens(a2)))
s: error
------------------------------
7471 | yes
h: exists a2.(exists a4.(exists a5.slecht(a5) & exists a6.verlicht(a6) & kamer(a4) & in(a2,a4)) & exists a3.(groep(a3) & mens(a2)))
p: (\Q.exists a3.(exists a5.(exists a6.(exists a8.((((\A F3000.A & B)(\A F3001.exists a10.(kaars(a10) & A(F3001))))(\a9.tafel(a9)))(a8) & aan(a6,a8)) & a5(a6)) & (((\A B.A & B)(\B.exists a7.(exists a8.donker(a8) & kamer(a7) & B(a7))))(\B.(exists a6.twee(a6) & vrouw(B))))(a5))(a3) & Q(a3)) & \Q.exists a2.(man(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\Q.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7475 | unknown
h: error
p: (\Q.exists a3.(exists a5.(exists a6.(exists a8.((((\A F3006.A & B)(\A F3007.exists a10.(kaars(a10) & A(F3007))))(\a9.tafel(a9)))(a8) & aan(a6,a8)) & a5(a6)) & (((\A B.A & B)(\B.exists a7.(exists a8.(kamer(a8) & a7(a8)) & B(a7))))(\B.(exists a6.twee(a6) & vrouw(B))))(a5))(a3) & Q(a3)) & \Q.exists a2.(man(a2) & Q(a2)))
s: error
------------------------------
7477 | yes
h: (\F3014.exists a3.((((\A F3016.A & B)(\Q.exists a6.(exists a7.vi(a7) & bierfles(a6) & Q(a6))))(exists a6.(exists a7.(exists a9.(tafel(a9) & aan(a7,a9)) & a6(a7)) & zonnebril(a6))))(a3) & F3014(a3)) & \F3013.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.zwart(a6) & hemd(a5) & B(a5))))(((\A B.A & B)((\B.exists a10.(man(a10) & B(a10)) & \B.exists a9.(zonnebril(a9) & B(a9)) & \B.exists a7.(exists a8.wit(a8) & hemd(a7) & B(a7)))))(\a4.man(a4))))(a2) & F3013(a2)))
p: \F3012.exists a1.((((\A B.A & B)(\Q.exists a4.(exists a5.vi(a5) & exists a6.(fles(a6) & bier(a4)) & Q(a4))))(((\A B.A & B)((\B.exists a7.(exists a9.(exists a10.(exists a12.(tafel(a12) & aan(a10,a12)) & a9(a10)) & zonnebril(a9))(a7) & B(a7)) & \B.exists a6.(exists a7.zwart(a7) & hemd(a6) & B(a6)))))(((\A B.A & B)((\B.exists a10.(man(a10) & B(a10)) & \B.exists a9.(zonnebril(a9) & B(a9)) & \B.exists a7.(exists a8.wit(a8) & hemd(a7) & B(a7)))))(\a4.man(a4)))))(a1) & F3012(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\F3014.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7501 | unknown
h: \B.(exists a1.vast(a1) & ((\B.exists a5.(exists a6.(bier(a6) & a5(a6)) & B(a5)) & \B.exists a4.(exists a5.(exists a6.rood(a6) & jas(a5) & a4(a5)) & B(a4)))(\B.exists a3.(persoon(a3) & B(a3))))(B))
p: error
s: error
------------------------------
7533 | unknown
h: (\A B.A & B)(\B.exists a2.(exists a4.((\B.exists a7.(exists a8.ander(a8) & jongen(a7) & B(a7)) & \B.exists a6.(exists a8.(exists a9.vast(a9) & exists a11.(man(a11) & naast(a8,a11)) & tuinslang(a8))(a6) & B(a6)))(a4) & exists z3029.(jongen(z3029) & a4(z3029)))(a2) & B(a2)))
p: error
s: error
------------------------------
7541 | unknown
h: error
p: exists a4.((exists a6.((((\A B.A & B)(\a9.bal(a9)))(\B.exists a8.(exists a10.(touchdown(a10) & voor(a8,a10)) & B(a8))))(exists b.persoon(b)))(a6) & exists z3035.paars(z3035) & trui(a6))(a4) & in(\B.exists a3.(-exists a4.(voetballer(a4) & a3(a4)) & B(a3)),a4))(\A.exists a1.(entity(a1) & A(a1)))
s: error
------------------------------
7544 | unknown
h: (((\A B.A & B)(\B.exists a4.(touchdown(a4) & B(a4))))(\B.exists a3.(bal(\C.met(a3,C)) & B(a3))))(\F3033.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.paars(a6) & trui(a5) & B(a5))))(\a3.voetballer(a3)))(a2) & F3033(a2)))
p: (((\A B.A & B)(\B.exists a4.(exists a5.(voetbal(a5) & a4(a5)) & B(a4))))(\B.exists a3.(exists a4.(ambtenaar(a4) & a3(a4)) & B(a3))))(\B.exists a2.(voetballer(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7546 | yes
h: lucht(\C.in(\A.A(\a2.springen(a2)),C),\F3039.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & exists a7.(gympak(a7) & a5(a7)) & B(a5))))(\B.(exists a4.jong(a4) & meisje(B))))(a2) & F3039(a2)))
p: lucht(\C.in(\A.A(\a2.springen(a2)),C),\F3038.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & gympak(a5) & B(a5))))(\B.(exists a4.jong(a4) & meisje(B))))(a2) & F3038(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    lucht(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7548 | yes
h: exists a2.(lucht(\C.in(a2,C)) & exists z3042.((((\A B.A & B)(\a5.blauw(a5)))(\B.(exists a4.jong(a4) & meisje(B))))(z3042) & a2(z3042)))
p: exists a2.(lucht(\C.in(a2,C)) & (((\A B.A & B)(\a5.blauw(a5)))(\B.(exists a4.jong(a4) & meisje(B))))(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (lucht(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7582 | yes
h: exists a2.(exists a3.(rugby(a3) & a2(a3)) & exists z3057.(man(z3057) -> a2(z3057)))
p: error
s: error
------------------------------
7590 | unknown
h: exists a2.(exists a4.(ongeluk(a4) & exists a7.(exists a8.ander(a8) & fietser(a7) & van(a4,a7)) & naar(a2,a4)) & fietser(a2))
p: error
s: error
------------------------------
7649 | no
h: (((\A B.A & B)(\a6.gras(a6)))(\A.A(\a4.rennen(a4))) & \B.exists a3.(exists a4.(exists a5.groen(a5) & voetbaltenue(a4) & a3(a4)) & B(a3)))(\B.exists a2.(exists a3.klein(a3) & jongen(a2) & B(a2)))
p: error
s: error
------------------------------
7667 | no
h: error
p: error
s: error
------------------------------
7677 | yes
h: (((\A B.A & B)(\B.(exists a4.(moeder(a4) & exists b.persoon(b)(a4)) & B(a4))))(\B.exists a3.(park(\C.in(a3,C)) & B(a3))))(\B.exists a2.(jongen(a2) & B(a2)))
p: park(\C.in(\B.exists a3.(exists a5.(jongen(a5) & exists b.persoon(b)(a5)) & met(a3,a5) & B(a3)),C),\B.exists a2.(exists a3.jong(a3) & moeder(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7718 | no
h: error
p: (bek(\C.in(\B.exists a3.(exists a4.(exists a5.super(a5) & soaker(a4) & a3(a4)) & B(a3)),C)) & exists a7.(hond(a7) & van(\C.in(\B.exists a3.(exists a4.(exists a5.super(a5) & soaker(a4) & a3(a4)) & B(a3)),C),a7)))(\B.exists a2.(man(a2) & B(a2)))
s: error
------------------------------
7720 | unknown
h: ((((\A B.A & B)(\B.exists a7.(spuitpistool(a7) & B(a7))))(\B.(bek(B) & exists a8.(exists a9.wit(a9) & hond(a8) & van(B,a8)))))(\C.in(\B.exists a3.(exists a4.(water(a4) & a3(a4)) & B(a3)),C)))(\B.exists a2.(man(a2) & B(a2)))
p: error
s: error
------------------------------
7726 | unknown
h: ((((\A B.A & B)(\B.exists a6.(paraplu(a6) & B(a6))))(\F3127 C.((((\A B.A & B)(\B.(exists a8.(vader(a8) & exists b.persoon(b)(a8)) & B(a8))))(\A.A(\a6.vasthouden(a6))))(F3127))(C)))(\B.exists a3.(exists a4.exists a5.(exists a6.blauw(a6) & jas(a5) & exists b.persoon(b)(a5))(a4) & a3(a4) & B(a3))))(\B.exists a3.(jongen(a3) & B(a3)))
p: error
s: error
------------------------------
7734 | unknown
h: exists a2.(exists a3.(exists a4.nieuw(a4) & wereld(a3) & a2(a3)) & exists z3129.(kind(z3129) & a2(z3129)))
p: error
s: error
------------------------------
7743 | unknown
h: (((\A B.A & B)(\B.exists a4.(sneeuwjacht(a4) & B(a4))))(\A.A(\a2.lopen(a2))))(\B.exists a2.(hond(a2) & B(a2)))
p: error
s: error
------------------------------
7772 | no
h: exists a2.(exists a4.(exists a5.klein(a5) & golf(a4) & op(a2,a4)) & surfer(a2))
p: exists a2.(exists a4.((((\A B.A & B)(\Q.exists a7.(exists a8.donkergroen(a8) & water(a7) & Q(a7))))(\B.(exists a6.groot(a6) & golf(B))))(a4) & op(a2,a4)) & exists z3148.(surfer(z3148) & a2(z3148)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a4 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7795 | yes
h: \F3161.(exists a1.links(a1) & exists a3.((\A B.A & B)(a3) & exists z3160.(tennisser(z3160) & a3(z3160)))(F3161))
p: error
s: error
------------------------------
7820 | unknown
h: exists a4.(stroom(a4) & in(\B C.B(\D.-spelen(D,C)),a4))(\B.exists a2.(hond(a2) -> B(a2)))
p: error
s: error
------------------------------
7877 | unknown
h: (((\A B.A & B)(\B.exists a4.(zandweg(a4) & B(a4))))(\B.exists a3.(exists a5.(paard(a5) & op(a3,a5)) & B(a3))))(\F3187.exists a2.((((\A B.A & B)(\a5.blauw(a5)))(\a3.man(a3)))(a2) & F3187(a2)))
p: (((\A B.A & B)(\B.exists a4.(exists a5.wit(a5) & paard(a4) & B(a4))))(\A.A(\a2.rijden(a2))))(\F3193.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & cowboyhoed(a5) & B(a5))))(\a3.man(a3)))(a2) & F3193(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7889 | yes
h: (\B.exists a3.(bal(a3) & B(a3)) & \Q.exists a2.(exists a4.(exists a5.(exists a7.(exists a8.bruin(a8) & hond(a7) & met(a5,a7)) & a4(a5)) & exists z3197.twee(z3197) & exists a5.wit(a5) & hond(a4))(a2) & Q(a2)))
p: (\B.exists a3.(tennisbal(a3) & B(a3)) & \Q.exists a2.(exists a3.twee(a3) & exists a5.(exists a6.(exists a8.(exists a9.bruin(a9) & hond(a8) & met(a6,a8)) & a5(a6)) & exists z3196.wit(z3196) & hond(a5))(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7932 | unknown
h: exists a4.(exists a5.druk(a5) & stadion(a4) & in(\B.exists a5.(vrouw(a5) & met(B,a5)),a4))(\Q.exists a2.(exists a3.vi(a3) & atleet(a2) & Q(a2)))
p: error
s: error
------------------------------
7937 | unknown
h: error
p: error
s: error
------------------------------
7938 | unknown
h: (\A B.A & B)((\F3226.exists a5.((\A B.A & B)(a5) & F3226(a5)) & \B.exists a4.(exists a6.(exists a7.(menigte(a7) & mens(a6)) & in(a4,a6)) & B(a4)))(\B.exists a3.(exists a4.elegant(a4) & vrouw(a3) & B(a3))))
p: \B.(exists a1.vast(a1) & exists a3.(exists a4.(bontsjaal(a4) & a3(a4)) & exists z3224.(exists a4.aziatisch(a4) & vrouw(z3224) & a3(z3224)))(B))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7947 | unknown
h: (((\A B.A & B)(((\A B.A & B)(\a7.strand(a7)))(\a5.water(a5))))(\A.A(\a2.rennen(a2))))(\B.exists a2.(jongen(a2) & B(a2)))
p: exists a4.(exists a5.ondiep(a5) & water(a4) & in(\A.A(\a2.spatten(a2)),a4))(\F3229.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.wit(a6) & tshirt(a5) & B(a5))))(\a3.kind(a3)))(a2) & F3229(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7950 | unknown
h: exists a4.(exists a5.ondiep(a5) & water(a4) & in(\A.A(\a2.spatten(a2)),a4))(\F3228.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.wit(a6) & tshirt(a5) & B(a5))))(\a3.jongen(a3)))(a2) & F3228(a2)))
p: (((\A B.A & B)(((\A B.A & B)(\a7.strand(a7)))(\a5.water(a5))))(\A.A(\a2.rennen(a2))))(\B.exists a2.(meisje(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7951 | unknown
h: (((\A B.A & B)(((\A B.A & B)(\a7.strand(a7)))(\a5.water(a5))))(\A.A(\a2.rennen(a2))))(\B.exists a2.(jongen(a2) & B(a2)))
p: exists a4.(exists a5.ondiep(a5) & water(a4) & in(\A.A(\a2.spatten(a2)),a4))(\F3228.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.wit(a6) & tshirt(a5) & B(a5))))(\a3.jongen(a3)))(a2) & F3228(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
7997 | unknown
h: water(\C.in(\A.A(\a2.spelen(a2)),C),\Q.exists a2.((((\A B.A & B)(\Q.exists a5.(zwempak(a5) & Q(a5))))(\a3.kind(a3)))(a2) & Q(a2)))
p: error
s: error
------------------------------
8057 | yes
h: error
p: error
s: error
------------------------------
8122 | unknown
h: \B.(exists a1.ontspannen(a1) & aan(\F3323.exists a3.(cheerleader(a3) -> F3323(a3)),B))
p: exists a2.(knie(\C.op(a2,C)) & exists a7.(exists a8.mannelijk(a8) & cheerleader(a7) & van(\C.op(a2,C),a7)) & exists z3319.(exists a3.vrouwelijk(a3) & cheerleader(z3319) & a2(z3319)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8138 | yes
h: (((\A B.A & B)(\a4.rug(a4)))((\B.exists a7.(tatoeage(a7) & B(a7)) & \B.exists a6.(oor(a6) & B(a6)))(\C.in(\B.exists a4.(exists a7.(piercing(a7) & (\Q.exists a8.(wenkbrauw(a8) & Q(a8)) & \Q.exists a7.(exists a8.rood(a8) & haar(a7) & Q(a7)))(a7))(a4) & B(a4)),C))))(\a2.meisje(a2))
p: (((\A B.A & B)(\a4.rug(a4)))((\B.exists a7.(tekening(a7) & B(a7)) & \B.exists a6.(oor(a6) & B(a6)))(\C.in(\B.exists a4.(exists a7.(exists a8.verschillend(a8) & piercing(a7) & (\Q.exists a8.(wenkbrauw(a8) & Q(a8)) & \Q.exists a7.(exists a8.rood(a8) & haar(a7) & Q(a7)))(a7))(a4) & B(a4)),C))))(\a2.meisje(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8141 | unknown
h: \F3331.exists a1.(aan((\Q.exists a5.(exists a6.rood(a6) & wenkbrauw(a5) & Q(a5)) & \F3330.exists a4.((((\A B.A & B)(\Q.exists a7.(exists a8.rood(a8) & haar(a7) & Q(a7))))(\a5.meisje(a5)))(a4) & F3330(a4))),a1) & F3331(a1))
p: (((\A B.A & B)(\a4.rug(a4)))((\B.-exists a7.(tatoeage(a7) & B(a7)) & \B.exists a6.(oor(a6) & B(a6)))(\C.in(\B.exists a4.(exists a7.(exists a8.verschillend(a8) & piercing(a7) & (\Q.exists a8.(wenkbrauw(a8) & Q(a8)) & \Q.exists a7.(exists a8.rood(a8) & haar(a7) & Q(a7)))(a7))(a4) & B(a4)),C))))(\a2.meisje(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F3331.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8163 | yes
h: error
p: error
s: error
------------------------------
8193 | no
h: \C.((buurt(\C.in(\A.A(\a3.verzamelen(a3)),C)) & exists a8.(buitenzitplaat(a8) & van(\C.in(\A.A(\a3.verzamelen(a3)),C),a8)))((\Q.exists a4.(kind(a4) & Q(a4)) & \a3.volwassen(a3))))(C)
p: error
s: error
------------------------------
8212 | unknown
h: (\B.exists a4.((\Q.exists a7.(exists a8.roze(a8) & kraal(a7) & Q(a7)) & \B.exists a6.(exists a7.zwart(a7) & shirt(a6) & B(a6)))(a4) & B(a4)) & \B.exists a3.(exists a5.(groep(a5) & in(a3,a5)) & B(a3)))(\B.exists a2.(meisje(a2) & B(a2)))
p: (((\A B.A & B)(\a4.wang(a4)))(\B.exists a3.(exists a4.(exists a5.(vlek(a5) & a4(a5)) & a3(a4)) & B(a3))))(\B.exists a2.(meisje(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8220 | unknown
h: (((\A B.A & B)(\B.(exists a4.hoog(a4) & gras(B))))(\A.A(\a2.lopen(a2))))(\Q.exists a2.(exists a3.twee(a3) & hond(a2) & Q(a2)))
p: (((\A B.A & B)(\a4.water(a4)))(\A.A(\a2.rennen(a2))))(\Q.exists a2.(exists a3.twee(a3) & hond(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8263 | no
h: (\Q.exists a3.(exists a5.(exists a6.(exists a8.(exists a9.(entity(a9) & exists a10.leeg(a10) & straat(a9))(a8) & op(a6,a8)) & a5(a6)) & voertuig(a5))(a3) & Q(a3)) & \Q.exists a2.(exists a3.(mens(a3) -> a2(a3)) & Q(a2)))
p: exists a4.(exists a5.druk(a5) & straat(a4) & in((\Q.exists a4.(voertuig(a4) & Q(a4)) & \Q.exists a3.(exists a4.(mens(a4) -> a3(a4)) & Q(a3))),a4))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\Q.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8313 | unknown
h: (\B.exists a4.(exists a5.(spel(a5) & a4(a5)) & B(a4)) & \B C.(exists a6.(kostuum(a6) & in(\A.A(\a4.kleden(a4)),a6))(B))(C))(\Q.exists a2.(kind(a2) & Q(a2)))
p: \F3396.exists a1.((((\A B.A & B)(\B.exists a4.(exists a5.(gezicht(a5) & exists a7.(exists a10.ander(a10) & kind(\C.naast(a7,C)) & a5(a7)) & a4(a5)) & B(a4))))(\B.(exists a3.jong(a3) & meisje(B))))(a1) & F3396(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8326 | no
h: error
p: exists a2.(-exists a3.(exists a4.(bmx(a4) & (exists a6.((((\A B.A & B)(\Q.exists a9.(zandhelling(a9) & Q(a9))))(\B.exists a8.(exists a10.(waterlichaam(a10) & voor(a8,a10)) & B(a8))))(exists b.persoon(b)))(a6) & biker(a6))(a3)) & a2(a3)) & exists a1.(entity(a1) & a2(a1)))
s: error
------------------------------
8334 | yes
h: exists a3.(exists a4.(truc(a4) & a3(a4)) & exists a4.(skateboard(a4) & op(a3,a4)))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: exists a3.(exists a4.(truc(a4) & a3(a4)) & exists a4.(skateboard(a4) & op(a3,a4)))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a3.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8343 | yes
h: (\B.exists a4.(exists a6.(exists a7.rood(a7) & motorfiets(a6) & op(a4,a6)) & B(a4)) & \B.exists a3.(exists a4.(helm(a4) & a3(a4)) & B(a3)))(\F3407.exists a2.((((\A B.A & B)(\B.exists a5.(motorcrossuniform(a5) & B(a5))))(\a3.persoon(a3)))(a2) & F3407(a2)))
p: (\B.exists a4.(exists a6.(exists a7.rood(a7) & motorfiets(a6) & op(a4,a6)) & B(a4)) & \B.exists a3.(exists a4.(helm(a4) & a3(a4)) & B(a3)))(\F3406.exists a2.((((\A B.A & B)(\B.exists a5.(motorcrossuniform(a5) & B(a5))))(\a3.man(a3)))(a2) & F3406(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8362 | unknown
h: \F3416.exists a1.(exists a3.(exists a4.(exists a6.(waterfontein(a6) & voor(a4,a6)) & a3(a4)) & (((\A B.A & B)(\B.exists a5.(exists a6.gestreept(a6) & shirt(a5) & B(a5))))(\a3.jongen(a3)))(a3))(a1) & F3416(a1))
p: \F3417.exists a1.(exists a3.(exists a4.(exists a6.(waterfontein(a6) & achter(a4,a6)) & a3(a4)) & (((\A B.A & B)(\B.exists a5.(exists a6.gestreept(a6) & shirt(a5) & B(a5))))(\a3.jongen(a3)))(a3))(a1) & F3417(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F3416.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8375 | unknown
h: exists a2.((((\A B.A & B)((\Q.exists a7.(rots(a7) & Q(a7)) & \Q.exists a6.(exists a7.besneeuwd(a7) & gras(a6) & Q(a6)))))(\A.A(\a3.op(a3))))(a2) & exists z3421.(exists a3.twee(a3) & hond(z3421) & a2(z3421)))
p: error
s: error
------------------------------
8383 | yes
h: exists a3.(exists a4.(exists a6.(glijbaan(a6) & van(a4,a6)) & a3(a4)) & (((\A B.A & B)(\a5.blauw(a5)))(\B.(exists a4.jong(a4) & meisje(B))))(a3))
p: (\A B.A & B)(exists a3.(exists a5.(exists a6.groen(a6) & glijbaan(a5) & van(a3,a5)) & exists z3428.((((\A B.A & B)(\a6.blauw(a6)))(\a4.meisje(a4)))(z3428) & a3(z3428))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a3 (exists a4 (exists a6 (glijbaan(a6) & van(a4,a6)) & a3(a4)) & (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8389 | unknown
h: exists a4.(exists a5.groot(a5) & stad(a4) & in(((\A B.A & B)(\B.exists a5.(gebouw(a5) & B(a5))))(\A.A(\a3.lopen(a3))),a4))(\B.exists a2.(exists a3.zwart(a3) & man(a2) & B(a2)))
p: exists a4.(exists a5.groot(a5) & stad(a4) & in(((\A B.A & B)(\B.exists a5.(gebouw(a5) & B(a5))))(\A.A(\a3.lopen(a3))),a4))(\B.exists a2.(exists a3.blank(a3) & man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8461 | unknown
h: exists a2.(grond(\C.op(a2,C)) & exists z3479.((((\A B.A & B)(\B.exists a5.(exists a6.achterwaarts(a6) & hoed(a5) & B(a5))))(\a3.man(a3)))(z3479) & a2(z3479)))
p: exists a2.(grond(\C.op(a2,C)) & exists z3483.((((\A B.A & B)(\Q.exists a5.(hoed(a5) & Q(a5))))(\a3.man(a3)))(z3483) & a2(z3483)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (grond(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8471 | yes
h: (\F3502.exists a4.((((\A B.A & B)(\B.(exists a9.grijs(a9) & haar(B))))(\B.(schouder(B) & exists a10.(man(a10) & van(B,a10)))))(\C.op(a4,C)) & F3502(a4)) & \B.exists a3.(exists a4.(exists a5.veelkleurig(a5) & exists a7.(a7(\z3499.vast(z3499)) & exists z3500.(stuk(z3500) & speelgoed(a7)))(a4) & a3(a4)) & B(a3)))(\F3498.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & trui(a5) & B(a5))))(\a3.meisje(a3)))(a2) & F3498(a2)))
p: (\F3496.exists a4.(schouder(\C.op(a4,C)) & exists a9.(exists a10.oud(a10) & (((\A B.A & B)(\B.(exists a13.grijs(a13) & haar(B))))(\a11.man(a11)))(a9) & van(\C.op(a4,C),a9)) & F3496(a4)) & \B.exists a3.(exists a4.(exists a5.veelkleurig(a5) & exists a7.(a7(\z3489.vast(z3489)) & exists z3490.(stuk(z3490) & speelgoed(a7)))(a4) & a3(a4)) & B(a3)))(\F3488.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & trui(a5) & B(a5))))(\a3.meisje(a3)))(a2) & F3488(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\F3502.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8500 | unknown
h: (\A B.A & B)(exists a3.(zee(a3) & persoon(a3)))
p: (\A B.A & B)(exists a3.(water(a3) & man(a3)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8505 | unknown
h: (((\A B.A & B)(\B.exists a4.(exists a5.warm(a5) & dag(a4) & B(a4))))(\B.exists a3.(exists a5.(parkban(a5) & op(a3,a5)) & B(a3))))(\Q.exists a2.(exists a3.twee(a3) & mens(a2) & Q(a2)))
p: (((\A B.A & B)(\B.exists a4.(exists a5.zonnig(a5) & dag(a4) & B(a4))))(\B.exists a3.(exists a5.(parkban(a5) & op(a3,a5)) & B(a3))))(\Q.exists a2.(exists a3.twee(a3) & mens(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8548 | unknown
h: exists a5.(blauw(a5) & in(\B.exists a4.(exists a5.(plons(a5) & a4(a5)) & B(a4)),a5))(\B.exists a3.(peuter(a3) & B(a3)))
p: exists a4.(exists a5.groot(a5) & exists a6.rood(a6) & zwembad(a4) & in(\B.exists a3.(exists a4.(water(a4) & a3(a4)) & B(a3)),a4))(\a2.kind(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8558 | unknown
h: exists a2.(exists a3.(exists a4.((((\A B.A & B)(\B.(exists a8.droog(a8) & gras(B))))(\B.(exists a6.zwart(a6) & hond(B))))(a4) & a3(a4)) & a2(a3)) & exists a3.bruin(a3) & hond(a2))
p: (\A B.A & B)(\B.exists a2.(exists a4.((\B.exists a8.(exists a9.bruin(a9) & hond(a8) & B(a8)) & \a7.gras(a7))(\C.in(a4,C)) & exists z3550.(exists a5.grijs(a5) & exists a6.zijdeachtig(a6) & hond(z3550) & a4(z3550)))(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 (exists a4 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8576 | yes
h: error
p: (((\A B.A & B)(\B.exists a4.(keukenaanrecht(a4) & B(a4))))(\F3563.exists a3.((\A B.A & B)(a3) & F3563(a3))))((\Q.exists a6.(exists a7.zwart(a7) & hond(a6) & Q(a6)) & \B.exists a5.(exists a6.klein(a6) & wit(a5) & B(a5)) & \B.exists a3.(exists a4.zwart(a4) & hond(a3) & B(a3))))
s: error
------------------------------
8632 | no
h: error
p: error
s: error
------------------------------
8633 | yes
h: error
p: (\B.(berekenen(B) & route(\C.van(B,C))) & exists a7.(\B.exists z3619.(a7(z3619) & B(z3619)) & \B.exists a6.(a7(a6) & B(a6))))(\C.aan(\B.exists a2.(man(a2) & B(a2)),C))
s: error
------------------------------
8658 | unknown
h: exists a2.(exists a4.(kermis(a4) & op(a2,a4)) & mens(a2))
p: (((\A B.A & B)(\a4.beurs(a4)))(exists z3624.(\B.(exists a4.z3624(exists b.persoon(b),a4) & B(a4)) & exists a5.(kraam(a5) & bij(z3624,a5)))))(\B.-exists a2.(exists a3.(groep(a3) & mens(a2)) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8660 | yes
h: error
p: (((\A B.A & B)(\Q.exists a4.(straat(a4) & Q(a4))))(\B.exists a3.(rij(\C.in(a3,C)) & B(a3))))(\B.exists a2.(exists a3.(groep(a3) & rolschaatser(a2)) & B(a2)))
s: error
------------------------------
8678 | yes
h: exists a2.(exists a3.(sprong(a3) & exists a6.(schans(a6) & van(a3,a6)) & a2(a3)) & exists z3635.(skateboarder(z3635) & a2(z3635)))
p: exists a2.(exists a4.(schans(a4) & van(a2,a4)) & exists z3634.(skateboarder(z3634) & a2(z3634)))
s:True | False 
------------------------------
8700 | unknown
h: exists a2.(exists a5.groen(a5) & gras(\C.in(a2,C)) & (((\A B.A & B)(\B.exists a5.(exists a6.geel(a6) & snavel(a5) & B(a5))))(\B.(exists a4.zwart(a4) & vogel(B))))(a2))
p: exists a2.(gras(\C.in(a2,C)) & (\Q.exists a4.(exists a5.oranje(a5) & vogel(a4) & Q(a4)) & \B.exists a3.(zwart(a3) & B(a3)))(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((exists a5 groen(a5) & gras(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8714 | yes
h: exists a2.(entity(a2) & a2(\z3649.rennen(z3649)))(\Q.exists a2.(exists a3.twee(a3) & exists a4.wit(a4) & hond(a2) & Q(a2)))
p: exists a1.(entity(a1) & (exists a3.snel(a3) & exists a3.(exists a4.twee(a4) & exists a5.wit(a5) & hond(a3) & lopen(a3)))(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a2.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8727 | yes
h: exists a2.(exists a4.(geluidsapparatuur(a4) & naar(a2,a4)) & exists z3652.(mens(z3652) -> a2(z3652)))
p: exists a2.(exists a4.(draaitafel(a4) & rond(a2,a4)) & exists z3650.(exists a3.(groep(a3) & mens(z3650)) & a2(z3650)))
s:False | False 
------------------------------
8786 | yes
h: error
p: (((\A B.A & B)(\B.exists a4.(stoep(a4) & B(a4))))(\B.exists a3.(exists a4.(touw(a4) & a3(a4)) & B(a3))))(\B.exists a2.(meisje(a2) & B(a2)))
s: error
------------------------------
8792 | unknown
h: error
p: error
s: error
------------------------------
8806 | yes
h: exists a4.(waterlichaam(a4) & in(\A.A(\a2.zwemmen(a2)),a4))(\B.exists a2.(dier(a2) & B(a2)))
p: exists a4.(waterlichaam(a4) & in(\A.A(\a2.zwemmen(a2)),a4))(\B.exists a2.(hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8832 | unknown
h: exists a2.(rand(\C.op(a2,C)) & exists a7.(balkon(a7) & van(\C.op(a2,C),a7)) & exists z3690.(man(z3690) & a2(z3690)))
p: exists a2.(richel(\C.op(a2,C)) & exists a7.(balkon(a7) & van(\C.op(a2,C),a7)) & exists z3691.(vrouw(z3691) & a2(z3691)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((rand(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8841 | unknown
h: exists a2.(exists a4.(gazon(a4) & over(a2,a4)) & exists z3696.(exists a3.groot(a3) & exists a4.wit(a4) & hond(z3696) & a2(z3696)))
p: exists a2.(exists a4.(gazon(a4) & over(a2,a4)) & exists z3695.(exists a3.klein(a3) & exists a4.wit(a4) & hond(z3695) & a2(z3695)))
s:False | False 
------------------------------
8855 | unknown
h: water(\C.in(\A.A(\a2.lopen(a2)),C),\F3702.exists a2.(exists a3.zwart(a3) & (((\A B.A & B)(\a6.lijn(a6)))(\a4.hond(a4)))(a2) & F3702(a2)))
p: (buurt(\C.in((\A.A(\a4.lopen(a4)) & \B.lijn(\C.aan(B,C))),C)) & water(\C.van(\C.in((\A.A(\a4.lopen(a4)) & \B.lijn(\C.aan(B,C))),C),C)))(\a2.hond(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    water(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
8938 | unknown
h: error
p: error
s: error
------------------------------
8963 | unknown
h: error
p: error
s: error
------------------------------
8986 | yes
h: exists a2.(strand(\C.op(a2,C)) & exists z3757.((((\A B.A & B)(\B.exists a5.(zwempak(a5) & B(a5))))(\B.(exists a4.jong(a4) & meisje(B))))(z3757) & a2(z3757)))
p: exists a2.(strand(\C.op(a2,C)) & exists z3755.((((\A B.A & B)(\B.exists a5.(bikini(a5) & B(a5))))(\B.(exists a4.jong(a4) & meisje(B))))(z3755) & a2(z3755)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (strand(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9014 | no
h: error
p: exists a1.(entity(a1) & ((\B.exists a5.(exists a6.(arm(a6) & exists b.persoon(b)(a6)) & a5(a6) & B(a5)) & (\A B.A & B)(\B.exists a5.(exists a7.(glijbaan(a7) & van(a5,a7)) & B(a5))))(\B.exists a3.(exists a4.blond(a4) & kind(a3) & B(a3))))(a1))
s: error
------------------------------
9029 | unknown
h: (((\A B.A & B)(\F3783.exists a4.(exists a6.(((\A B.A & B)(\B.exists a9.(exists a10.rotsachtig(a10) & oever(a9) & op(B,a9))))(a6) & exists z3782.zwart(z3782) & hond(a6))(a4) & F3783(a4))))(\A.A(\a2.lopen(a2))))(\B.exists a2.(exists a3.bruin(a3) & hond(a2) & B(a2)))
p: exists a4.(bos(a4) & in(\A.A(\a2.spelen(a2)),a4))(\Q.exists a2.(exists a3.twee(a3) & hond(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9036 | unknown
h: (((\A B.A & B)(\B.exists a4.(exists a5.rotsachtig(a5) & strand(a4) & B(a4))))(\A.A(\a2.spelen(a2))))(\Q.exists a2.(exists a3.twee(a3) & hond(a2) & Q(a2)))
p: exists a3.(exists a4.(exists a5.gouden(a5) & (((\A B.A & B)(\A.A))(\a6.hond(a6)))(a4) & a3(a4)) & exists z3795.(exists a4.wit(a4) & hond(z3795) & a3(z3795)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9056 | unknown
h: (\A B.A & B)(exists a3.((\Q.exists a6.(exists a7.groen(a7) & exists a8.(tong(a8) & a6(a8)) & Q(a6)) & \Q.exists a5.(blauw(a5) & Q(a5)))(a3) & exists z3804.(exists a4.twee(a4) & kind(z3804) & a3(z3804))))
p: error
s: error
------------------------------
9069 | yes
h: exists a2.((((\A B.A & B)(\a7.strand(a7)))(\a5.water(a5)))(\C.in(a2,C)) & exists z3814.(exists a3.twee(a3) & jongen(z3814) & a2(z3814)))
p: error
s: error
------------------------------
9093 | unknown
h: exists a2.(exists a3.(exists a5.(exists a6.(exists a8.(oorlog(a8) & exists a11.mens(exists b.persoon(b),a11) & aan(a8,a11) & uit(a6,a8)) & a5(a6)) & exists z3820.ander(z3820) & ding(a5))(a3) & a2(a3)) & exists z3821.(veteraan(z3821) & a2(z3821)))
p: exists a2.(exists a4.(exists a5.militair(a5) & accessoirewinkel(a4) & in(a2,a4)) & exists z3818.(exists a3.groot(a3) & man(z3818) & a2(z3818)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 (%%START ERROR%%exists a5.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9102 | unknown
h: exists a4.(grasveld(a4) & in(((\A B.A & B)(\B.(exists a5.(hoofd(a5) & exists b.persoon(b)(a5)) & B(a5))))(\B.exists a4.(exists a5.(voetbal(a5) & a4(a5)) & B(a4))),a4))(\B.exists a2.(exists a3.grijs(a3) & hond(a2) & B(a2)))
p: (\A B.A & B)(exists a3.(bal(\C.met(a3,C)) & exists z3829.((((\A B.A & B)(\B.exists a6.(exists a7.blauw(a7) & halsband(a6) & B(a6))))(\a4.hond(a4)))(z3829) & a3(z3829))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9125 | unknown
h: exists a2.((\Q.exists a5.(sieraad(a5) & Q(a5)) & \B.exists a4.(exists a5.kleurrijk(a5) & overhemd(a4) & B(a4)))(a2) & exists z3841.(vrouw(z3841) & a2(z3841)))
p: error
s: error
------------------------------
9132 | yes
h: exists a2.(exists a4.(sportschool(a4) & in(a2,a4)) & exists z3851.((((\A B.A & B)(\B.exists a5.(exists a6.zwart(a6) & trui(a5) & B(a5))))(\a3.man(a3)))(z3851) & a2(z3851)))
p: \F3849.exists a1.(exists a3.(exists z3848.(exists a6.(sportschool(a6) & in(z3848,a6)) & a3(z3848)) & (exists a4.exists a6.(zwart(a6) & exists b.persoon(b)(a6))(a4) & (((\A B.A & B)(\B.exists a6.(trui(a6) & B(a6))))(\a4.man(a4)))(a4))(a3))(a1) & F3849(a1))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a4 (sportschool(a4) & in(a2,a4)) & exists z3851 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9136 | yes
h: (\B.exists a4.(exists a5.(trui(a5) & a4(a5)) & B(a4)) & \B.exists a3.(exists a5.(sportschool(a5) & in(a3,a5)) & B(a3)))(\B.exists a2.(man(a2) & B(a2)))
p: exists a2.(exists a4.(sportschool(a4) & in(a2,a4)) & exists z3851.((((\A B.A & B)(\B.exists a5.(exists a6.zwart(a6) & trui(a5) & B(a5))))(\a3.man(a3)))(z3851) & a2(z3851)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9169 | unknown
h: (((\A B.A & B)(\a4.weg(a4)))(\A.A(\a2.lopen(a2))))((\Q.exists a4.(exists a5.wit(a5) & hond(a4) & Q(a4)) & \B.exists a3.(exists a4.klein(a4) & bruin(a3) & B(a3))))
p: (((\A B.A & B)(\a4.stoep(a4)))(\A.A(\a2.lopen(a2))))((\Q.exists a4.(exists a5.wit(a5) & hond(a4) & Q(a4)) & \B.exists a3.(exists a4.klein(a4) & bruin(a3) & B(a3))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9188 | unknown
h: (\A B.A & B)(exists a3.(exists a5.(bal(a5) & achter(a3,a5)) & exists z3875.(exists a4.geel(a4) & hond(z3875) & a3(z3875))))
p: (\B.exists a4.(exists a5.(exists a6.(tennisbal(a6) & a5(a6)) & a4(a5)) & B(a4)) & \B.exists a3.(gras(\C.op(a3,C)) & B(a3)))(\B.exists a2.(hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9198 | unknown
h: (\F3891 C.((((\A B.A & B)(\Q.exists a7.(schoolkind(a7) & Q(a7))))(\A.A(\a5.omringen(a5))))(F3891))(C) & \B.exists a3.(exists a5.(straat(a5) & op(a3,a5)) & B(a3)))(\a3.dame(a3))
p: exists a2.(exists a4.(exists a5.(groep(a5) & kind(a4) & exists a8.(exists a9.stenen(a9) & huis(a8) & naast(a4,a8))) & voor(a2,a4)) & exists z3884.((((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & spijkerbroek(a5) & B(a5))))(\a3.vrouw(a3)))(z3884) & a2(z3884)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\F3891 C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9200 | unknown
h: exists a2.(exists a4.(exists a5.(groep(a5) & kind(a4) & exists a8.(exists a9.stenen(a9) & huis(a8) & naast(a4,a8))) & voor(a2,a4)) & exists z3886.((((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & spijkerbroek(a5) & B(a5))))(\a3.man(a3)))(z3886) & a2(z3886)))
p: (\F3887 C.((((\A B.A & B)(\Q.exists a7.(schoolkind(a7) & Q(a7))))(\A.A(\a5.omringen(a5))))(F3887))(C) & \B.exists a3.(exists a5.(straat(a5) & op(a3,a5)) & B(a3)))(\B.exists a2.(dame(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a4 (exists a5 (groep(a5) & (kind(a4) & exists a8 ((exists a9 stenen(a9) & huis(a8)) & naast(a4,a8)))) & voor(a2,a4)) & exists z3886 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9211 | unknown
h: exists a4.(exists a5.bosrijk(a5) & omgeving(a4) & in(\B.exists a3.(lucht(\C.in(a3,C)) & B(a3)),a4))(\B.exists a2.(kerel(a2) & B(a2)))
p: exists a4.(hout(a4) & in(\B.exists a3.(lucht(\C.in(a3,C)) & B(a3)),a4))(\B.exists a2.(kerel(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9224 | unknown
h: (exists a4.(bek(a4) & exists b.persoon(b)(a4)) & in(\B.exists a3.(exists a4.(exists a5.blauwwit(a5) & bal(a4) & a3(a4)) & B(a3)),a4))(\B.(exists a3.zwart(a3) & hond(B)))
p: (((\A B.A & B)(\B.exists a4.(bal(a4) & B(a4))))(\A.A(\a2.rennen(a2))))(\B.exists a2.(hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%exists a4.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9242 | unknown
h: error
p: exists a2.(exists a3.(voertuig(a3) & a2(a3)) & exists a4.(exists a5.(exists a7.(foto(a7) & voor(a5,a7)) & a4(a5)) & (((\A B.A & B)(\a6.blauw(a6)))(\a4.man(a4)))(a4))(a2))
s: error
------------------------------
9287 | unknown
h: sneeuw(\C.in(\F3940.exists a5.(exists a7.(((\A B.A & B)(\B F3937.exists a10.(aan(B,a10) & F3937(a10))))(a7) & reling(a7))(a5) & van(F3940,a5)),C),\B.exists a2.(man(a2) & B(a2)))
p: (\B.exists a5.(exists a7.(rood(a7) & over(a5,a7)) & B(a5)) & \B.exists a4.(exists a5.(exists a7.(a7(\z3948.af(z3948)) & heuvel(a7))(a5) & a4(a5)) & B(a4)))(\B.exists a3.(man(a3) & B(a3)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    sneeuw(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9303 | yes
h: exists a2.(lucht(\C.in(a2,C)) & exists z3959.(skateboarder(z3959) & a2(z3959)))
p: exists a2.(lucht(\C.in(a2,C)) & skateboarder(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (lucht(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9314 | unknown
h: (((\A B.A & B)(\B.exists a4.(snowboard(a4) & B(a4))))(\B.exists a3.(exists a5.(acrobatiek(a5) & aan(a3,a5)) & B(a3))))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: (((\A B.A & B)(\B.exists a5.(exists a6.lang(a6) & betonnen(a5) & B(a5))))(\B.exists a4.(exists a6.(beneden(a6) & naar(a4,a6)) & B(a4))))(\B.exists a3.(snowboarder(a3) & B(a3)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9336 | unknown
h: error
p: error
s: error
------------------------------
9359 | yes
h: \F3989.exists a1.(exists a2.(surfer(a2) & (((\A B.A & B)(\B.exists a5.(exists a6.enorm(a6) & golf(a5) & B(a5))))(\A B.exists a3.(A(a3) & B(a3))))(a1)) & F3989(a1))
p: (((\A B.A & B)(\B.exists a4.(exists a5.groot(a5) & golf(a4) & B(a4))))(\A.A(\a2.surfen(a2))))(\B.exists a2.(surfer(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F3989.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9371 | unknown
h: (((\A B.A & B)(\B.exists a4.(exists a5.europees(a5) & staat(a4) & B(a4))))(\A.A(\a2.lopen(a2))))((\Q.exists a4.(exists a5.(kaki(a5) & broek(a4)) & Q(a4)) & \F3995.exists a3.((((\A B.A & B)(\B.exists a6.(exists a7.rood(a7) & jas(a6) & B(a6))))(\a4.man(a4)))(a3) & F3995(a3))))
p: (buurt(\C.in(\A.A(\a2.lopen(a2)),C)) & exists a7.(rotswand(a7) & van(\C.in(\A.A(\a2.lopen(a2)),C),a7)))((\B.exists a4.(exists a5.zwart(a5) & rugzak(a4) & B(a4)) & \F3990.exists a3.((((\A B.A & B)(\Q.exists a6.(capuchon(a6) & Q(a6))))(((\A B.A & B)(\B.exists a7.(exists a8.rood(a8) & jas(a7) & B(a7))))(\a5.persoon(a5))))(a3) & F3990(a3))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9380 | unknown
h: exists a2.((\Q.exists a7.(exists a9.(a9(\z4000.op(z4000)) & exists a10.(a10(\z3999.wit(z3999)) & \B.exists a9.(a10(a9) & B(a9)))(a9))(a7) & Q(a7)) & \B.exists a6.(man(a6) & paars(\C.in(a6,C)) & B(a6)) & \B.exists a4.(voetbal(a4) & B(a4)))(a2) & exists z4001.((((\A B.A & B)(\a5.groen(a5)))(\a3.man(a3)))(z4001) & a2(z4001)))
p: exists a2.(voetbal(\C.voor(a2,C)) & speler(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((%%START ERROR%%\Q.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9401 | unknown
h: (\B.exists a4.(camera(\C.voor(a4,C)) & B(a4)) & \B.exists a3.((\Q.exists a6.(exists a7.zwart(a7) & exists a8.(leren(a8) & chap(a6)) & Q(a6)) & \B.exists a5.(exists a6.paars(a6) & shirt(a5) & B(a5)))(a3) & B(a3)))(\B.exists a2.(man(a2) & B(a2)))
p: error
s: error
------------------------------
9424 | unknown
h: \B.exists a1.(exists a3.(exists a7.(exists a8.lucht(\C.in(exists b.persoon(b),C),a8) & a7(a8) & zand(a7))(\C.in(a3,C)) & exists z4008.(hond(z4008) & a3(z4008)))(a1) & B(a1))
p: error
s: error
------------------------------
9425 | no
h: error
p: error
s: error
------------------------------
9433 | yes
h: (\A B.A & B)(exists a3.((\A B.A & B)(a3) & exists z4012.(exists a4.zwartwit(a4) & hond(z4012) & a3(z4012))))
p: exists a4.(exists a5.groen(a5) & tuin(a4) & in(\A.A(\a2.lopen(a2)),a4))(\B.(exists a3.zwartwit(a3) & hond(B)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9452 | unknown
h: (schaduw(\C.in(\A.A(\a2.springen(a2)),C)) & boom(\C.van(\C.in(\A.A(\a2.springen(a2)),C),C)))(\B.exists a2.(hond(a2) & B(a2)))
p: land(\C.in(\B.exists a3.(lucht(\C.in(a3,C)) & B(a3)),C),\B.exists a2.(hond(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (schaduw(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9453 | unknown
h: error
p: (schaduw(\C.in(\A.A(\a2.springen(a2)),C)) & boom(\C.van(\C.in(\A.A(\a2.springen(a2)),C),C)))(\B.exists a2.(hond(a2) & B(a2)))
s: error
------------------------------
9490 | no
h: error
p: exists a2.(exists a4.((((\A B.A & B)(\Q.exists a7.(exists a8.bruin(a8) & gras(a7) & Q(a7))))(\a5.veld(a5)))(a4) & in(a2,a4)) & exists z4028.(cluster(z4028) & exists a5.(exists a6.vi(a6) & exists a7.bruin(a7) & hond(a5) & van(z4028,a5)) & a2(z4028)))
s: error
------------------------------
9500 | unknown
h: park(\C.in(\B.exists a3.(exists a4.(dutje(a4) & a3(a4)) & B(a3)),C),\a2.hond(a2))
p: (((\A B.A & B)(\Q.exists a4.(straat(a4) & Q(a4))))(\B.exists a3.(exists a5.(jas(a5) & op(a3,a5)) & B(a3))))((\Q.exists a4.(exists a5.wit(a5) & exists a6.gevlekt(a6) & hond(a4) & Q(a4)) & \B.exists a3.(exists a4.groot(a4) & bruin(a3) & B(a3))))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    park(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9545 | unknown
h: error
p: error
s: error
------------------------------
9571 | yes
h: exists a2.(exists a4.(bank(a4) & op(a2,a4)) & exists z4066.(exists a3.oud(a3) & man(z4066) & a2(z4066)))
p: (\B.exists a4.((\B.exists a7.(exists a8.zwart(a8) & broek(a7) & B(a7)) & \B.exists a6.(exists a7.grijs(a7) & jas(a6) & B(a6)))(a4) & B(a4)) & \B.exists a3.(exists a5.(bank(a5) & op(a3,a5)) & B(a3)))(\B.exists a2.(exists a3.oud(a3) & man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9584 | yes
h: (((\A B.A & B)(\a4.schildersezel(a4)))(\B.exists a3.(verfkwast(a3) & B(a3))))(\a2.dame(a2))
p: (((\A B.A & B)(\a4.schildersezel(a4)))(\B.exists a3.(verfkwast(a3) & B(a3))))(\a2.vrouw(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9623 | unknown
h: (((\A B.A & B)(\Q.exists a4.(exists a5.bloot(a5) & voet(a4) & exists a8.(tennisbaan(a8) & op(a4,a8)) & Q(a4))))((\A.A(\a4.lopen(a4)) & \B.exists a4.(exists a5.(exists a6.blauw(a6) & shirt(a5) & a4(a5)) & B(a4)))))(\B.exists a2.(vrouw(a2) & B(a2)))
p: (((\A B.A & B)(\B.exists a6.(tennisbaan(a6) & B(a6))))(\B.exists a5.(exists a6.(\B.exists z4075.(a6(z4075) & B(z4075)) & a5(a6)) & B(a5))) & \B.exists a3.(exists a4.(exists a5.blauw(a5) & shirt(a4) & a3(a4)) & B(a3)))(\B.exists a2.(man(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9669 | yes
h: error
p: error
s: error
------------------------------
9677 | unknown
h: error
p: error
s: error
------------------------------
9706 | no
h: veld(\C.in(\A.A(\a2.rennen(a2)),C),\F4109.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.groot(a6) & tak(a5) & B(a5))))(\B.(exists a4.zwartwit(a4) & hond(B))))(a2) & F4109(a2)))
p: exists a2.(veld(\C.in(a2,C)) & exists z4112.((((\A B.A & B)(\B.exists a5.(exists a6.groot(a6) & tak(a5) & B(a5))))(\B.(exists a4.zwartwit(a4) & hond(B))))(z4112) & a2(z4112)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    veld(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9713 | yes
h: veld(\C.in(\A.A(\a2.rennen(a2)),C),\F4109.exists a2.((((\A B.A & B)(\B.exists a5.(exists a6.groot(a6) & tak(a5) & B(a5))))(\B.(exists a4.zwartwit(a4) & hond(B))))(a2) & F4109(a2)))
p: exists a2.(exists a3.(exists a4.enorm(a4) & stok(a3) & exists a8.groen(a8) & gras(\C.op(a3,C)) & a2(a3)) & exists z4116.(exists a3.zwartwit(a3) & hond(z4116) & a2(z4116)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    veld(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9722 | unknown
h: error
p: (((\A B.A & B)(\A.A))(\A.A(\a3.lopen(a3))))(\B.exists a3.(jongen(a3) & B(a3)))
s: error
------------------------------
9745 | unknown
h: error
p: error
s: error
------------------------------
9747 | yes
h: error
p: error
s: error
------------------------------
9759 | unknown
h: \F2323.exists a1.(exists a3.(exists a4.(exists a6.(exists a7.hoog(a7) & cementmuur(a6) & op(a4,a6)) & a3(a4)) & (((\A B.A & B)(\B.exists a5.(exists a6.blauw(a6) & jas(a5) & B(a5))))(\a3.persoon(a3)))(a3))(a1) & F2323(a1))
p: (\B C.exists a5.(exists a7.(water(a7) & met(a5,a7)) & B(a5))(C) & \B.exists a3.(exists a4.(exists a6.(a6(\z208.vast(z208)) & waterpistool(a6))(a4) & a3(a4)) & B(a3)))(\B.exists a2.(exists a3.(kind(a3) & a2(a3)) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\F2323.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9763 | unknown
h: \C.((((\A B.A & B)(\a5.vrouw(a5)))(\A.A(\a3.berijden(a3))))(\a2.olifant(a2)))(C)
p: exists a4.(schijf(a4) & in(\B.exists a3.(paddenstoel(a3) & B(a3)),a4))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9771 | unknown
h: (\A B.A & B)((\B.exists a5.(exists a7.(exists a8.(stuk(a8) & speelgoed(a7)) & achter(a5,a7)) & B(a5)) & ((\A B.A & B)(\B.exists a6.(veld(a6) & B(a6))))(\A.A(\a4.rennen(a4))))(\B.exists a3.(hond(a3) & B(a3))))
p: (((\A B.A & B)(\B.exists a4.(speelgoedauto(a4) & B(a4))))(\B.exists a3.(exists a5.(straat(a5) & op(a3,a5)) & B(a3))))(\Q.exists a2.(exists a3.twee(a3) & exists a4.klein(a4) & kind(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9788 | unknown
h: (\B.exists a4.(camera(\C.naar(a4,C)) & B(a4)) & \B.exists a3.(exists a4.(exists a6.(a6(\z3325.vast(z3325)) & drank(a6))(a4) & a3(a4)) & B(a3)))(\B.exists a2.(exists a3.(groep(a3) & mens(a2)) & B(a2)))
p: exists a2.(exists a4.(exists a5.elektrisch(a5) & gitaar(a4) & op(a2,a4)) & exists z616.(man(z616) & a2(z616)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9789 | unknown
h: (\B.exists a4.(exists a5.(foto(a5) & a4(a5)) & B(a4)) & exists a5.(penseel(a5) & in(\A.A(\a3.hurken(a3)),a5)))(\B.exists a2.(man(a2) & B(a2)))
p: \F3547.(exists a1.vast(a1) & exists a3.(exists a4.(exists a5.regenboogkleurig(a5) & exists a6.afghaans(a6) & tapijt(a4) & a3(a4)) & (\Q.exists a5.(paars(a5) & Q(a5)) & \F3546.exists a4.((((\A B.A & B)(\a7.goud(a7)))(\a5.meisje(a5)))(a4) & F3546(a4)))(a3))(F3547))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9822 | unknown
h: exists a2.(exists a3.iemands(a3) & snowboard(a2) & lucht(\C.in(a2,C)) & exists z460.(exists a3.(springer(a3) & z460(a3)) & a2(z460)))
p: (((\A B.A & B)(\B.exists a4.(fiets(a4) & B(a4))))(\A.A(\a2.rijden(a2))))(\Q.exists a2.(exists a3.twee(a3) & mens(a2) & Q(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 ((exists a3 iemands(a3) & (snowboard(a2) & lucht(%%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9838 | unknown
h: exists a3.(exists a5.(verf(a5) & met(a3,a5)) & exists a2.(exists a4.jong(a4) & exists a4.topless(a4) & vrouw(a2) & a3(a2)))
p: \C.((((\A B.A & B)(\B.exists a5.(band(a5) & B(a5))))(\A.A(\a3.bespelen(a3))))(\B.exists a2.(instrument(a2) -> B(a2))))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    %%START ERROR%%\C.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9843 | unknown
h: (\F1231.exists a3.((((\A B.A & B)(\B.exists a6.(exists a7.(pak(a7) & staan(a6) & exists a10.(microfoon(a10) & bij(a6,a10))) & B(a6))))(\a4.man(a4)))(a3) & F1231(a3)) & \a1.zingen(a1))
p: (((\A B.A & B)(\a4.automaat(a4)))(\B.exists a3.(exists z3318.(\B.(exists a4.z3318(exists b.persoon(b),a4) & B(a4)) & a3(z3318)) & B(a3))))(\B.exists a2.(familie(a2) & B(a2)))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (%%START ERROR%%\F1231.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9869 | unknown
h: (((\A B.A & B)(\B.exists a4.(zandheuvel(a4) & B(a4))))(\B.exists a3.(exists a5.(crossmotor(a5) & op(a3,a5)) & B(a3))))(\A B.(exists a1.A(exists b.persoon(b),a1) & B(a1)))
p: \C.exists a3.(exists a5.(aap(a5) & over(a3,a5)) & exists a2.(fiets(a2) & a3(a2)))(C)
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9880 | unknown
h: (((\A B.A & B)(\a4.weg(a4)))(\A.A(\a2.dansen(a2))))(\B.exists a2.(man(a2) & B(a2)))
p: error
s: error
------------------------------
9931 | unknown
h: exists a2.(exists a3.(gitaar(a3) & a2(a3)) & exists z1823.(kind(z1823) & a2(z1823)))
p: exists a2.(exists a4.(exists a5.elektrisch(a5) & gitaar(a4) & op(a2,a4)) & exists z1228.(vrouw(z1228) & a2(z1228)))
s:False | False 
------------------------------
9963 | unknown
h: exists a2.(exists a4.(politiemotor(a4) & op(a2,a4)) & agent(a2))
p: (((\A B.A & B)(\a4.gras(a4)))(\A.A(\a2.grazen(a2))))(\a2.dier(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    (((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9975 | unknown
h: exists a2.(exists a3.(instrument(a3) & a2(a3)) & exists z3910.((((\A B.A & B)(\B.exists a5.(band(a5) & B(a5))))(\a3.meisje(a3)))(z3910) & a2(z3910)))
p: exists a2.(waterdruppel(\C.naar(a2,C)) & hond(a2))
s: (FATAL)
%%ERROR: A term cannot be constructed from the marked string:


    exists a2 (exists a3 (instrument(a3) & a2(a3)) & exists z3910 ((((%%START ERROR%%\A B.%%END ERROR%%

Fatal error:  sread_term error
------------------------------
9988 | unknown
h: error
p: (\A B.A & B)(exists a3.(exists a4.(crossmotor(a4) & exists a7.(zandheuvel(a7) & van(a4,a7)) & a3(a4)) & exists z3373.(exists a4.jong(a4) & man(z3373) & a3(z3373))))
s: error
------------------------------
