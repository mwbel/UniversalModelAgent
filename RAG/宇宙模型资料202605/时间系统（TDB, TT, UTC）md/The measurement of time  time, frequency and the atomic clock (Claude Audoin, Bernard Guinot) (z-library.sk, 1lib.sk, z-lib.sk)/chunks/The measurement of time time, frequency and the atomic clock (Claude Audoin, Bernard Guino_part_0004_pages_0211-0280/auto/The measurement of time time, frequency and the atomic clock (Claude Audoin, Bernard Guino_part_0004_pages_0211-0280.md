but on the frequency of the quartz oscillator. Note that, in reality, the transfer function of the operational filter is not as simple as we have assumed here. However, this does not afect the general features of the servo loop considered.

The conclusions at the end of Section 6.4.1c also apply. The servo controlled oscillator reproduces the fast frequency variations of the non-controlled quartz and the slow frequency changes of the atomic reference.

# (e) Automatic tuning of the resonant cavity

As mentioned in Section 6.5.3b,asevere restriction is imposed on the cavity tuningfrequency,if theoscillation frequency is toremain constant.This is why most hydrogen masers are now equipped with cavity auto-tuning systems. We shall give here a brief description of the three procedures used to achieve this goal.

In each case, an error signal is obtained. It is proportional to the extent to which the cavity is detuned with respect to the value procuring an oscillation frequency equal to the atomic transition frequency. The error signal acts on a varicap coupled to the cavity.

The first method is based on measurements of the oscillation frequency of the auto-tuned maser. It requires the use of a second maser as a reference. Generally,the roles of the two masers are exchanged at regular intervals. In the other two methods, however, information concerning cavity tuning is deduced directly from the behaviour of the maser itself.

First method: atomic flux modulation. This method is also known as spinexchange tuning. It uses the broadening of the atomic resonance that results from collisions between confined hydrogen atoms,with electron, and hence spin exchange. It is the most direct method and makes use of (6.109) giving the change in oscillation frequency as a function of the cavity tuning frequency $\nu _ { \mathrm { c } } = \omega _ { \mathrm { c } } / 2 \pi$ [6.71, 6.72].

The atomic flux is slowly modulated, with period of the order of a few hundred seconds, between two values having associated quality factors $Q _ { \mathrm { a t 1 } }$ and $Q _ { \mathrm { a t } 2 }$ .Figure 6.25 shows that the variation in the oscillation frequency is proportional to $\Delta \nu _ { \mathrm { c } }$ , that it changes sign with $\Delta \nu _ { \mathrm { c } }$ ,and that it vanishes when the condition $\nu _ { \mathrm { c } } = \nu _ { 0 }$ is satisfied. The error signal is obtained as the output of a reversible counter. This device counts the beat frequency between the maser to becontrolled and the reference maser,counting positively for half the modulation period and negatively for the following half period.

In general, the change $\Delta \nu _ { 0 2 } - \Delta \nu _ { 0 1 }$ in the oscillation frequency is smaller than the maser frequency shift associated with cavity detuning. The latter is equal to $\Delta \nu _ { 0 1 }$ or $\Delta \nu _ { 0 2 }$ ,depending on whether the quality factor of the atomic resonance is Qat1 or Qat2, respectively (Figure 6.25). Furthermore, measurement of △vo2 -△vol is perturbed by random frequency fluctuations in both the maser to be controlled and the reference maser. Consequently, the latter must also be a hydrogen maser, to ensure a satisfactory signal-to-noise ratio in the measurement of this quantity.

In practice, the time constant for the correction to the cavity tuning frequency of the controlled maser is of the order of one hour. For sampling periods $\tau$ less than about one hour, the frequency stability of the maser is degraded. The benefits of this control system are manifested only in the longer term, for $\tau$ greater than one day.

Second method: modulation of the cavity resonance frequency. This method uses the inertia of the amplitude of the magnetic moment of the atoms, discussed in Section 6.5.3b [6.69]. It is a consequence of the high values, close to one second,of the relaxation times $T _ { 1 }$ and $T _ { 2 }$

The cavity resonance frequency is square wave modulated, with period a few hundredths of a second, much shorter than $T _ { 1 }$ and $T _ { 2 }$ .The electromagnetic field in the cavity represents the cavity response to excitation by the oscillating magnetic moment. Schematically, it is just as though this excitation had constant amplitude and frequency. The response depends on the cavity tuning frequency. The level of oscillation is therefore modulated,unless the variation in the cavity tuning frequency is centered on the atomic transition frequency. An error signal is obtained if this condition is not fulfilled. It can be used to servo control the cavity tuning frequency in such a way that the oscillation frequency equals the atomic transition frequency.

This method guarantees the detection of any cavity detuning with a satisfactory signal-to-noise ratio. The control time constant for the cavity is of the order of one hour. The medium term frequency stability is almost unaffected, and slow drifts in the cavity tuning frequency,and hence in the maser oscillation frequency, are suppressed.

Third method: direct control of the cavity resonance frequency. Suppose for the moment that the resonant cavity contained no hydrogen atoms. We could then use one of the known methods for servo controlling thecavity resonance frequency at a preassigned value. One way would be to apply the method described in Section 6.4.1c, shown schematically in Figure 6.9. but replacing the atomic resonance curve by the cavity response curve. Practically speaking,afrequencymodulatedsignal isinjectedintoteavitywithfrecy variation $\Delta \nu _ { 0 } ^ { \prime }$ about the mean frequency.

For the application to hydrogen masers, care must be taken to ensure that the signal thereby introduced into the cavity does not perturb the oscillation. To this end,it is crucial to suppress the carrier frequency of theapplied signal, whose frequency would be equal to the atomic transition frequency. This is achieved very simply when the modulating waveform of the cavity interrogation signal isa square wave. In this case,the carrier frequency is eliminated when the modulation frequency is an even submultiple of the modulation depth $\Delta \nu _ { 0 } ^ { \prime }$ [6.73]. This condition can easily be satisfied using frequency synthesis techniques.Infact,thecavity interrogationsignal issynthesised fromthesignal delivered by the quartz oscillator, whose frequency is servo controlled at the frequency of the maser oscillation.

The cavity interrogation signal may have greater intensity than the maser oscillation. Itfollows thatwhen the cavity is detuned,theerror signalexhibitsa good signal-to-noise ratio. In practice, the cavity control time constant may be short, of the order of $1 0 ~ \mathrm { s } .$ Long termfrequency stability isimproved,without significantly affecting medium term frequency stability [6.74].

# 6.5.4 Passive hydrogen maser

When the auto-oscillation condition is not satisfied, that is, when $I \ < \ I _ { \mathrm { { t } } }$ ,the maser behaves as an amplifier. The resonant cavity is supplied by a signal at 1.42...GHz, produced by an external generator. The response of the standard is just the amplified signal. The maser therefore becomes a passive frequency standard with a highly selective frequency response.

# (a) Maser gain

In order to model the external excitation applied to the cavity at angular frequency $\omega$ ,a source term must be added to the right hand side of (6.107) [6.4]. The complex amplitude of the magnetic field in the cavity is then a solution of

$$
\left[ \omega _ { \mathrm { c } } ^ { 2 } - \mathrm { i } \omega \frac { \omega _ { \mathrm { c } } } { Q _ { \mathrm { c } } } - \omega ^ { 2 } \right] B ( \omega ) = \frac { \mu _ { 0 } \eta } { V _ { \mathrm { c } } } \omega ^ { 2 } M ( \omega ) - \frac { \omega _ { \mathrm { c } } ^ { 2 } } { Q _ { \mathrm { c } } } B _ { \mathrm { e } } ( \omega ) \ ,
$$

where $M ( \omega )$ is still given by (6.104). The extra term is such that, when there are no atoms and when we have $\omega = \omega _ { \mathrm { c } }$ , the magnetic field,with complex amplitude $B ^ { \prime } ( \omega )$ has the same modulus as $B _ { \mathrm { e } } ( \omega )$ .We set

$$
\mathrm { i } B ^ { \prime } ( \omega ) = B _ { \mathrm { e } } ( \omega ) ~ .
$$

The complex gain of the amplifier is the ratio of the value of $B ( \omega )$ when there are atoms to its value $B ^ { \prime } ( \omega )$ when there are none. To simplify, we assume that

![](images/02019b99c14cceb7e2275f46708bb2e064ff081b5360cb1d056d33ab29aa5af0.jpg)  
Fig. 6.28. Non-saturated gain of the passive hydrogen maser.

the cavity is tuned to the atomic resonance frequency and restrict discussion to the case where the saturation factor is much smaller than unity. We then obtain

$$
| G ( \omega ) | = \left[ 1 + \frac { \alpha ( \alpha - 2 ) } { 1 + T _ { 2 } ^ { 2 } ( \omega - \omega _ { 0 } ) ^ { 2 } } \right] ^ { - 1 / 2 }
$$

for the modulus of the non-saturated gain, where we have defined

$$
\alpha = \frac { I } { I _ { \mathrm { t } } } \ .
$$

Figure 6.28 shows how the modulus of the non-saturated gain varies with the value of $\omega \mathrm { ~ - ~ } \omega _ { 0 }$ for several values of $\alpha$ . At resonance, the gain varies monotonically from 1, when $\alpha = 0$ , to infinity, when $\alpha = 1$ . In the first case, the maser response is simply that of the resonant cavity. In the second case, the oscillation threshold is reached. The resonance curve narrows as the oscillation threshold is approached. Its width at half-maximum is $2 / T _ { 2 }$ for very small values of $\alpha$ . It tends to zero when $\alpha$ approaches unity.

# (b) Resonance frequency

In the passive hydrogen maser, the coupling between the electromagnetic field and the atomic medium is also very strong since the later amplifies the electromagnetic field injected into the cavity. In practice,the dependence of the atomic resonance frequency on the cavity tuning frequency is also given by (6.109) [6.75]. Here $\omega$ must be interpreted as the angular frequency of the atomic transition,as observed when the angular resonance frequency of the cavity is $\omega _ { \mathrm { c } }$ ·

# (c) Practical construction of the atomic resonator

Active and passive masers differ essentially through the volume of their resonant cavities.In order to reduce this volume by a factor of the order of 10, materials must be introduced into the cavity whose losses make it imposible to obtain a quality factor greater than $1 5 \times 1 0 ^ { 3 }$ ，

The oscillation condition can no longer be satisfied and the maser must thereafter beoperated passively. (However,itispossble toincrease thequality factor electronically by means of a $Q$ -amplifying circuit, insuch a way that the oscillation condition can be satisfied.This method has been implemented, but is not currently used.)

Naturally,every effort is made to reduce the volumes of other parts of the maser,without significantly changing their structure with respect to the active maser. We shall therefore consider only the various solutions adopted for greatly reducing the cavity volume. These are shown schematically in Figure 6.29.

The cavity can be partially filled by a ring-shaped block of alumina or sapphire (Figure6.29a)[6.76,6.77].Inthis case,thedielectric material serves asa support for an external metallic coating and also for an internal Teflon coating. These define the boundaries of the resonant cavity and the atom storage cell, respectively.

Another alternative is to introduce metal electrodes into the resonant cavity. These surround the storage cell. They have the shape of cylindrical sectors. In one approach they are rigidly fixed to the cell, without touching the outer envelope of the cavity (Figure 6.29b) [6.78]. In another variant, they are connected to the outer walls of the cavityby radial metal struts (Figure 6.29c)[6.79]. The cavity structure then resembles a magnetron structure. It is easier to reproduce and more rigid than the one shown in Figure 6.29b.

![](images/a78a9a99b335ce7807c100943febebc7cf9d26e4dcaa944093174ce3d001eaf5.jpg)  
Fig. 6.29. Resonant cavities for passive hydrogen masers.In (c), field lines lie outside the plane of the cross section.

# (d)Frequencycontrolofaquartzoscilatorand servocontrolof thecavity resonance frequency

The quartz oscillator could be servo controlled just by transposing the method used in the caesium clock. In this case, the $1 . 4 2 \dots \mathrm { G H z }$ interrogation signal would be very slowly modulated, at a frequency of the order of $0 . 1 \ \mathrm { H z }$ less than the width of the atomic resonance. This method is not the best, because the modulated interrogation signal would be perturbed by flicker frequency noise. Indeed, the closer the spectral components of the modulated signal lie to the carrier frequency, the more they are affected by this kind of noise. In addition, the time constant of the quartz oscillator frequency control must be large compared with the modulation period, and it would then have too great a value.

In a pasive hydrogen maser, resonance is observed by the changing amplitude of the electromagnetic field in a resonant cavity. The interrogation frequency can then be stabilised using a variant of Pound's method [6.80]. This method is commonly used at ultrahigh frequencies and in magnetic resonance experiments. In contrast to the method mentioned above, the modulation frequency must be much higher than the resonance width of the reference. The drawbacks described above are thus removed. Using the present variant, both the quartz oscillator frequency and the cavity tuning frequency can be servo controlled at the atomic resonance. The cavity frequency must be stabilised,because itsstructure means thatithasa highthermal exaion coefficient.

![](images/c32b719547561fc63372cabe328726af71461f3f5689a29c74b315422811b8f8.jpg)  
Fig. 6.30. Passive hydrogen maser. Schematic diagram showing how the quartz oscillatorand maser cavity can be servo controlled.

Figure 6.30 shows the electronics in a highly simplified way. The interrogation signal,produced viathe quartz scillator,is modulatedatafrequency $\nu _ { \mathbf { M } }$ close to $1 5 \mathrm { k H z }$ .This is much higher than the atomic resonance width and it has the same order of magnitude as half the pass band of the resonant cavity. The amplitude and phase shift of the transmitted carrier wave depend on the difference between its frequency and the atomic resonance frequency.Likewise, the amplitude and phase difference of the lateral lines are functions of the cavity resonance frequency.

At the cavity output, the signal is amplified. Its various spectral components interfere in a quadratic detector. The detected signal.is modulated and the component at the modulation frequency $\nu _ { \mathrm { M } }$ is extracted. Two circuits, each introducing an appropriate phase shift, then separate those components expressing the deviation between the carrier frequency and the atomic resonance frequency,on the one hand,and the carrier frequency and the cavity resonance frequency, on the other [6.81]. These two signals are then demodulated in synchronism with the modulation applied to the interrogation signal. Two error signals are thereby produced. After integration, one controls the quartz oscillator frequency and the other the cavity resonance frequency.

# 6.5.5 Metrological properties of the hydrogen maser

# (a) Medium term frequency instability

For sampling times less than about $0 . 1 \ s$ ,the frequency instability of the hydrogen maser,whether it is active or passive,is roughly the same as that of the quartz oscillator servo controlied by the atomic resonance. When $\tau > 0 . 1 \ \leq$ S， we must distinguish the two cases of active and passive masers.

Active maser. In the active hydrogen maser, the electromagnetic field in the resonant cavity induces an atomic magnetic moment which then maintains the electromagnetic field. However, thermal noise occurs in the cavity resonance mode and the associated random electromagnetic field perturbs generation of a coherent oscillation. The noise component in phase with the oscillation creates a frequency fluctuation. It can be shown that the power spectral density of the relative frequency fluctuations (Section 5.2.2) is given by [6.4, 6.82]

$$
S _ { y } ( f ) = \frac { k T } { P _ { \mathrm { a t } } Q _ { \mathrm { a t } } ^ { 2 } } \ ,
$$

where $k$ is Boltzmann's constant, $T$ is the thermodynamic temperature of the cavity, $P _ { \mathrm { a t } }$ is the power dissipated in the cavity,and $\mathcal { Q } _ { \mathrm { a t } }$ is the quality factor of the atomic resonance. This is white frequency noise. Table 5.2 shows that the Allan deviation of the frequency fluctuations is then equal to

$$
\sigma _ { y } ( \tau ) = { \frac { 1 } { Q _ { \mathrm { a t } } } } \left( { \frac { k T } { 2 P _ { \mathrm { a t } } } } \right) ^ { 1 / 2 } \tau ^ { - 1 / 2 } .
$$

This expression describes the medium term frequency instabilityfor t greater than about $1 0 \mathrm { ~ s ~ }$ . In the shorter term, for $\tau$ between 0.1 and $1 0 \ \mathrm { s } .$ frequency instability is related to the low power supplied by the maser. We must then consider the effect of random signals adding to the oscillation signal. These arise from thermal noise in the cavity itself and from noise contributed by circuitsamplifying the signal delivered by the maser.Thecomponents of these fluctuations in quadrature with the oscilltion produce frequency fluctuations in theobservable signal.The power spectral densityof therelative frequency fluctuations is then equal to

$$
S _ { y } ( f ) = \frac { 4 k T } { P _ { \mathrm { a t } } } \frac { f ^ { 2 } } { \nu _ { \mathrm { 0 } } ^ { 2 } } \left( 1 + F \frac { P _ { \mathrm { a t } } } { P _ { \mathrm { r } } } \right) ,
$$

where $\nu _ { 0 }$ is the oscillation frequency. The parameter $F$ is the amplifer noise factor and $P _ { \Gamma }$ the power efctively received by the amplifier.The Allan standard deviation associated with this white phase noise is

$$
\sigma _ { y } ( \tau ) = \frac { 3 k T f _ { \mathrm { h } } } { 2 \pi \nu _ { 0 } ^ { 2 } P _ { \mathrm { a t } } } \left( 1 + F \frac { P _ { \mathrm { a t } } } { P _ { \mathrm { r } } } \right) \tau ^ { - 1 } ,
$$

where $f _ { \mathrm { h } }$ is the cutof frequency of the device used to observe frequency fluctuations.The standard deviationsadd quadratically.

Typically, when the cutoff frequency of the device measuring frequency stability isequal toewrtzeve $\sigma _ { y } ( \tau ) \sim 1 0 ^ { - 1 3 } \tau ^ { - 1 }$ for $\tau \ < \ 1 0 \ s$ and $\sigma _ { y } ( \tau ) \sim 3 \times 1 0 ^ { - 1 4 } \tau ^ { - 1 / 2 }$ for $\tau > 1 0 \mathrm { s }$ ,as shown in Figure 6.11.

Passive maser. Although the method used to servo control the quartz oscillator by the atomic resonance is not the same as the one used in the caesium clock,equation (6.63) remains valid to the nearest order of magnitude.For the passive maser,

$$
\sigma _ { y } ( \tau ) = \frac { K } { Q _ { \mathrm { a t } } } \left( \frac { k T } { P _ { \mathrm { a t } } } \right) ^ { 1 / 2 } \tau ^ { - 1 / 2 } ,
$$

where $K$ is a constant of the order of 10, that depends on experimental conditions. In practice, we have $\sigma _ { y } ( \tau ) \sim 1$ to $2 \times 1 0 ^ { - 1 2 } \tau ^ { - 1 / 2 }$ for $1 < \tau < 1 0 ^ { 5 }$ S [6.83].

(b)Residual frequency shifts

The first three frequency shifts that we shall consider are common to all types of atomic frequency standard. The last three are specific to the hydrogen maser.

Second order Zeeman effect. The static magnetic field $B _ { 0 }$ applied parallel to the ultrahigh frequency magnetic field shifts the energy levels (Figure 6.2).

T'his Zeeman effeet is second order for levels with $m \kappa = 0$ The frequency shift is

$$
\Delta 1 \nu _ { \ell } = 2 . 7 7 3 0 \dot { \times } 1 0 ^ { 1 1 } B _ { 0 } ^ { 2 } .
$$

Where $I _ { \{ \} }$ 1s given in teslas. $i _ { 0 }$ is usually close to $1 ( ) \cdot$ T This means that $( 1 ^ { \circ } , 1 ^ { \circ } ) 1 . ( ) > 1 0 ^ { \circ }$ The value of this frequeney shift is measured by causing low frequeney transitions .V/ O. .Vmt t 1 between sublevels of 1he triplet $1 : 1$ . In praetice. relative uncertainty in the value of this frequeney shift is less than 10-13.

Second order Doppler effect. This frequeney shift of relativistic origin is related to the motion of the atoms relative to the laboratory reference frame. The hydrogen atoms are therimalised by impaets with the storage cell wall and their Kinetic energy is 3k T 2. From (6.1o). the frequeney shit is then given by

$$
{ \frac { \Delta \mathfrak { v } \mathfrak { p } } { \mathfrak { v } _ { 0 } } } = - { \frac { 3 k T } { 2 M \mathfrak { c } ^ { 2 } } } \ ,
$$

where $. 1 l$ is the mass of the hydrogen atom. Assuming that the temperature of the storage cel walls is 313 K. this gives .Nrp ro - $+ . 3 1 > 1 0 1 1$ . Although this trequeney shitt is the largest affeeting the hydrogen maser. if the cell wall temperature is measured to the nearest O.1 K. it leads to an evtremely low uneertainty in the value of the frequeney shitt. equal to $1 . + \cdot 1 ( ) 1 +$

Cavity pulling. This is deseribed by $( ( 7 , 1 0 0 ) )$ and has already been diseussed in some detail. When the cavity is carefully tuned. either manually or automatically the uncertainty introduced by this effect is less than $1 0 ^ { - 1 4 }$

Colisions between hydrogen atons. Colisions between hydrogen atoms induee a shitt in the hypertine transition frequeney. This frequency shitt can be almost completely compensated for by suitable manual or autonatic cavity tuning methods. so that the residual effeet on the frequeney delivered by the hydrogen maser is a few times 10 13.

Magnetie relaxation. A frequeney shitt is produced when the hydrogen atoms move through the utrahigh frequeney and statie magnetie tield gradients. The shift depends on the value of these gradients. the value of the statie tield and the composition of the atomie beam. When care is taken to produee as uniform a static magnetic ticld as possible. this frequeney shift is lessthan 1o 13 for $B _ { 0 } = 1 0 ^ { - 7 } \mathrm { T }$

Collisions with the storage bulb walls. Collision with the wall of the storage bulb modifies the phase of the induced dipolar moment of the atom. The corresponding frequency shift has the form

$$
\Delta \nu _ { \mathrm { w } } = \frac { K } { D } ,
$$

where $K$ is a constant depending on the properties of the coating and the temperature, whilst $D$ is the diameter of the storage bulb. As an example, $K \ \sim \ - 0 . 4 \ \mathrm { H z } \ \mathrm { c m }$ at $4 0 ^ { \circ } \mathrm { C }$ for FEP 120 Teflon produced by Dupont de Nemours. Hence, $\Delta \nu _ { \mathrm { w } } / \nu _ { 0 } \sim - 1 . 9 \times 1 0 ^ { - 1 1 }$ for $D = 1 5 ~ \mathrm { c m }$ This shift can be measured, in principle, by varying $D$ . In practice,difficulties involved in reproducing the coating lead to an uncertainty of the order of $10 \%$ in the value of the frequency shift due to collisions with the walls.

# (c) Long term frequency instability and inaccuracy

Long term frequency instability. In the long term,frequency instability results from systematic effects connected with dimensional instability of the resonant cavity and variations in the wall effect [6.84]. The first mentioned cause of instability leads toafrequencydriftoftheorderof $1 0 ^ { - 1 6 }$ to $1 0 ^ { - 1 5 }$ per day. Thelatter is of litle importance for certain applications,such as very long baseline radio interferometry. For timekeeping,an automatic cavity tuning system must be implemented. The second cause of instability is related to the slowly changing properties of the fluorine-containing polymer used to line the storage bulb.The corresponding change in the frequency is also of the order of $1 0 ^ { - 1 6 }$ Lto $1 0 ^ { - 1 5 }$ per day. These variations can occur in opposite directions.

Long term instability of the hydrogen maser depends on whether it is active or passive,and also on the manufacturer. The most stable in the long term are the active type with cavity auto-tuning.Hydrogen masers have been achieved with long term stability similar to that of caesium beam primary standards.

Inaccuracy. The accuracy of the hydrogen maser characterises its capacity to deliver without calibration a frequency agreeing with the hyperfine transition frequency $\nu _ { \mathrm { H } }$ in the unperturbed ground state hydrogen atom.

In practice, inaccuracy is determined by uncertainty in the value of the frequency shift due to hydrogen atom collisions with the storage bulb walls. It is close to or =2-5× 10-12.

The value of $\nu _ { \mathrm { H } }$ ,resulting from measurement rather than from a definition as in the caesium case,is tainted with uncertainty. Its standard deviation is equal to $3 \mathrm { m H z }$ in absolute value (Table 6.1),or $\sigma _ { 2 } = 2 \times 1 0 ^ { - 1 2 }$ in relative value. The standard deviation of the uncertainty in the frequency delivered by a hydrogen

maser is thus $O \mathrm { H }$ given by

$$
\sigma _ { \mathrm { H } } = \left( \sigma _ { 1 } ^ { 2 } + \sigma _ { 2 } ^ { 2 } \right) ^ { 1 / 2 } .
$$

# 6.5.6 Cryogenic hydrogen masers

In many areas of activity, it would be useful to have a frequency standard even more stable than current state-of-the-art hydrogen masers.For example, a frequency generator with improved medium and long term frequency stability would be very helpful in studying the metrological properties of the cold atom fountain clock (Sections 6.4.3 and 6.4.4) and the confined mercury ion clock (Section 6.7.3). Such a generator could also satisfy the needs of deep space navigation and it could be used for more accurate measurement of gravitational frequency snifts, with a view to distinguishing the various predictions of lgeneral relativity.

Since(6.120) and (6.122) show that the short and medium term frequency instability of the active hydrogen maser are increasing functions of cavity temperature, it would clearly be advantageous to cool the resonant cavity. Concerning the long term frequency instability, it is known that the dimensional stability of materials is improved at low temperatures.Likewise, we may hope to improve the stability of the properties of the material lining the storage cell, if there is a way of continually renewing it. These varied reasons have stimulated several studies of the properties of the hydrogen maser at low temperatures, down to $4 . 2 ~ \mathrm { K }$

However, the most decisive results with regard to a highly stable hydrogen maser were obtained from fundamental physical studies of the hydrogen atom. It was observed that recombination and relaxation of this atom are much reduced on a helium film at temperatures below $1 \mathrm { \textrm { K } }$ In addition, the frequency shift due to collisions on the film is of the same order of magnitude as in masers operating at room temperature, and the broadening of the hyperfine resonance due to collisions between hydrogen atoms is three orders of magnitude smaler, at equal densities, than at room temperature. The atomic quality factor $\mathcal { Q } _ { \mathrm { a t } }$ and the power $P _ { \mathrm { a t } }$ dissipated in the cavity can therefore be significantly increased. Equations (6.120) and (6.122) show that such increases would contribute to reducing the frequency instabilityof the maser,just ike a temperaturereduction. From the results,it was estimated that the frequency instability of a cryogenic hydrogen maser at $0 . 5 ~ \mathrm { K }$ could be of the order of $1 0 ^ { - 1 8 }$ for $\tau = 1 0 ^ { 3 }$ s [6.85]. However, the prediction was made under the assumption that previously presented theoretical results would still apply. In reality, this is not the case. At $0 . 5 ~ \mathrm { K }$ , the helium pressure is such that the mean free path of the hydrogen atoms would be of the order of just 1 cm. Hydrogen atoms would no longer average out spatial variations in the static and ultrahigh magnetic fields. Furthermore,additional frequency shifts appear.These result from increased collision time between hydrogen atoms,which itself arises because theaverage relative velocities of the atoms are smaller at low temperatures.Further studies are thus required.

In order to build a cryogenic hydrogen maser,a helium dilution refrigerator must be used. This is therefore diffcult and costly. One of these masers has been used for fundamental physical measurements [6.86]. At the time of writing,it has not been possible to construct two cryogenic hydrogen masers with the qualities required for metrological assessment via mutual comparison.

# 6.6 Rubidium cell clocks

Optical detection of the hyperfine structure transition in alkali atoms contained in a sealed resonance cell was first studied in the USA at the end of the 1950s [6.87,6.88, 6.89]. During the same period, the first alkali vapour frequency standards were built [6.90, 6.91]. It was immediately realised that compact atomic frequency standards could be made and the first commercial models appeared at the beginning of the 1960s [6.92]. In these manufactured devices, the rubidium atom was preferred to other alkali atoms for practical reasons.

The market for rubidium cell atomic clocks turned out to be quite sizeable and many companies have produced or still produce this type of atomic frequency standard. Annual production amounts to several thousand instruments. The emphasis has been on high-performance devices that are both reliable and compact.They may be as small as $0 . 2 5 \mathrm { d m } ^ { 3 }$ (Table 6.2) [6.93,6.94].

By its very structure, the rubidium cell clock is a secondary atomic frequency standard (i.e.,its frequency must be calibrated with respect to a primary source). Its long term frequency instability lies between that of a quartz oscillator and a caesium beam clock. It is mainly used in positioning,navigation and telecommunications systems.

# 6.6.1 Description

The rubidium clock is a passive-type standard. It uses the double resonance method,i.e.,optical and microwave resonances,and is shown shematicallyin Figure 6.31.

A small lamp, with volume less than $1 ~ \mathrm { c m } ^ { 3 }$ ,contains about $1 ~ \mathrm { m g }$ of rubidium 87 or a mixture of isotopes 85 and 87, together with a noble gas such as krypton. A discharge is produced by coupling with a radiofrequency generator. The operating temperature lies between 125 and $1 4 0 ^ { \circ } \mathrm { C }$

![](images/5aa6a021c9885f5ed1df24bb01f75e25dc731ce9f00a49f633760ddc4e962420.jpg)  
Fig. 6.31. Schematic diagram of the rubidium cell clock.

In the version shown in Figure 6.30, the light passes through a hyperfine filter. This contains rubidium 85 and a noble gas such as argon at a pressure of around $1 0 ^ { 4 }$ Pa.

The resonance cell, with a volume of a few $\mathrm { c m } ^ { 3 }$ , contains rubidium 87. A low pressure buffer gas (at about $1 0 ^ { 3 }$ Pa) is also present. This consists of a mixture of nitrogen and rare gases.

In the design described here, the hyperfine filter is separate. More compact versions incorporate hyperfine filtering into the resonance cell itself. The latter then contains natural rubidium, composed of $72 \%$ rubidium 85 and $28 \%$ rubidium 87 and the hyperfine filter is said to be integrated. The quantity of rubidium contained in the resonance cell is very small, of the order of one milligram.

This cell is placed in a resonant cavity tuned to the hyperfine transition frequency of the rubidium 87 atom, i.e., about 6834.68 MHz. It receives the microwave interrogation signal. Various procedures are implemented to obtain a suitable electromagnetic field configuration in the cell, whilst reducing the volume of the cavity as far as possible. For example, a cavity structure like the one shown in Figure $6 . 2 9 \mathrm { c }$ can be used. The two parallel cavity walls have holes pierced in them to let through the light produced by the lamp. The temperature of the resonance cell is maintained at about $8 0 ^ { \circ } \mathrm { C }$

The light intensity transmitted bythecellis measuredusingasiliconphoto electric detector. When the frequency of the interogation signal varies about the rubidium 87 hyperfine transition frequency, the variation in the current delivered by the photoelectric cell has the form of an upside down resonance curve.

![](images/bd9210a2be205ba34192d63b37425ea0b6752f8ad9f432d2bb5a5beb1fccc69f.jpg)  
Fig.6.32.Rubidiumclock. (a)Spectrum emitted by rubidiumlamp.(b)Filtered spec trum. (c) Optical pumping in the cell.

Magnetic shielding protects the cellfrom the surrounding magnetic field and itsfluctuations.Suitablyarrangedcoils withinthisshieldingcreateamagetic field of about $1 0 ^ { - 5 }$ T.

# 6.6.2 Operating principles

Complex physical mechanisms take place inside the resonance cell. These arise from the double resonance and the presence of a buffer gas.We shall present only a highly simplified explanation of the atomic resonator,illustrated in Figure 6.32.

In the lamp, rubidium 87 atoms emit resonance lines $\mathrm { D } _ { 1 }$ and $\mathrm { D } _ { 2 }$ with wavelengths 795 and $7 8 0 ~ \mathrm { n m }$ ,respectively. These have a hyperfine structure resulting from the existence of two hyperfine levels $F = 1$ and $F = 2$ in the ground state.Figure 6.32a shows the light spectrum emitted by the lamp in a rather simplified way.

By a favourable isotopic coincidence, rubidium 85 atoms in the hyperfine filter absorb one of the hyperfine components in each of the $\mathrm { D } _ { 1 }$ and $\mathrm { D } _ { 2 }$ lines, so that the filter is opaque to these components of the light spectrum emitted by the lamp whilst remaining transparent to the other components. The rare gas contained in the filter shifts and broadens the rubidium 85 resonance lines.Its pressure is adjusted so as to optimise filtering efficiency. Figure 6.32b shows the light spectrum transmitted by the filter.

In the resonance cell, the incident light is selectively absorbed by those rubidium 87 atoms in the $F ~ = ~ 1$ hyperfine level of the ground state (see

Sections 6.2.2b and c). Once the atoms have been excited in this way and thereby enter one of the P states, they relax into the two levels of the ground state,either by fluorescence, or by collisions with nitrogen atoms,the latter being the predominant mechanism.† The absorption-relaxation cycle depopulates the $F = 1$ level in favour of the $F = 2$ level. Figure 6.32c represents the optical pumping cycle thus set up. The cell is transparent to the incident light since the number of atoms capable of absorbing that light has become small.

Up to now, we have not mentioned the ultrahigh frequency field in the cavity. The above description is still valid when this field no longer resonates with the transition between the two hyperfine sublevels of the ground state. Let us now suppose that the frequency of the interrogation signal equals the frequency of the hyperfine transition. The transition $F = 2  F = 1$ is stimulated and the $F = 1$ level is thereby repopulated. A fraction of the incident light is absorbed and the light intensity reaching the photocell is slightly reduced in consequence. Figure 6.31 shows the resonance profile that appears when the microwave signal frequency sweeps across the atomic resonance frequency. This Lorentzian profile can be described by the equation

$$
I = I _ { \mathrm { n } } \left[ 1 - \frac { k } { 1 + 4 ( \nu - \nu _ { 0 } ) ^ { 2 } / \Delta \nu ^ { 2 } } \right] ,
$$

where $I$ is the flux of photons collected, which equals $I _ { \Omega }$ outside resonance. The width at half-maximum of the resonance is $\Delta \nu$ ,of the order of $5 0 0 ~ \mathrm { H z }$ and $k$ is a parameter close to $0 . 5 \%$

The buffer gas in the resonance cell plays several important roles. Apart from the non-radiative decay of rubidium 87,it suppresses Doppler broadening of the hyperfine resonance (Section 6.2.3b). In addition, it reduces the rate at which atoms collide with the cell walls, thereby reducing the relaxation and frequency shift associated with such collsions. The buffer gas pressure is arranged so that difusion velocities of rubidium atoms are very small, of the order of $1 ~ \mathrm { c m ~ s ^ { - 1 } }$ . To all intents and purposes,the rubidium atoms are stationary during their relaxation time of around 1 ms. They cannot therefore average out the value of the optical and microwave fields crossing the cell. In consequence, the properties of te cell are not homogeneous and this greatly complicates quantitative analysis.

Whenhyperfefltgisdutintresonaneliself,sp in compact designs,unwanted hyperfine components intheincident lightare progressively atenuated along the light trajectory, so that a detailed treatment of the behaviour of the clock is even more complicated.

# 6.6.3 Electronics

As the rubidium clock is a passive atomic frequency standard, the atomic resonance can be used to control the frequency of a quartz oscillator in the same way a in acaesiumbeam clock (Section 6.4.1c).Other electrical circuits produce the radiofrequency signal required to excite the lamp discharge. Separate thermal control of the lamp,the resonance cell and the hyperfine filter (if it exists separately) is essential. This makes it possible to adjust the rubidium density and gas pressure contained in the various parts of the instrument, guaranteeing satisfactory operation of the lamp,a sufficient signal-to-noise ratio to allow detection of the hyperfine resonance,and control over undesirable frequency shifts.

# 6.6.4 Metrological properties of rubidium cell clocks

# (a) Medium term frequency instability

As for any passive frequency standard,an approximation to the medium term frequency instability is provided by (6.63). Here, the noise is shot noise in the electrical current supplied by the photocell. To the nearest power of ten, we have $Q _ { \mathrm { { a t } } } \sim 1 0 ^ { 7 }$ and $( P _ { \mathrm { S } } / P _ { \mathrm { N } } ) ^ { 1 / 2 } \sim 2 \times 1 0 ^ { 3 }$ in a pass band of $1 \ \mathrm { H z }$ ,implying Oy(τ)\~10-11τ-1/2.

In practice, medium term frequency instability takes values between $5 \times 1 0 ^ { - 1 2 } \tau ^ { - 1 / 2 }$ and $1 0 ^ { - 1 0 } \tau ^ { - 1 / 2 }$ dependingothemaufacturer.Forampling periods $\tau$ greater than $1 0 ^ { 3 }$ or $1 0 ^ { 4 }$ S, $\sigma _ { y } ( \tau )$ no longer varies as $\tau ^ { - 1 / 2 }$ because of theinfluence of systematic effects.Figure6.11compares thetypical frequency instability of rubidium cell clocks with that of other atomic clocks.

# (b)Shifts in the atomic transition frequency

Apart from those frequency shifts common to all atomic clocks,two particularly detrimental frequency shifts are specific to the rubidium cell clock. One is typical of double resonance experiments where two transitions sharing the same energy level are simultaneously excited.Itiscalled the light shift because it is associated with optical pumping. The other is due to collisions between rubidium atoms and molecules of the buffer gas,where interaction forces induce a change in the hyperfine splitting.

Light shift. This effect vanishes when the pumping light spectrum is centred on the rubidium absorption line. This condition depends on the composition and content of the lamp and hyperfine filter, if there is one,or the resonance cell,otherwise. In practice, the light shift can never be completely suppressed. It amounts to a few hertz.

Shift due to collisions. This frequency shift is proportional to the buffer gas pressure. In typical conditions, it is of the order of one kilohertz. Its value changes from one clock to the next because it is impossible to control the composition and pressure of the buffer gas accurately enough when the cells are being filled and sealed.

However, rubidium cell clocks deliver a signal with predetermined nominal frequency,e.g., $1 0 \mathrm { M H z }$ .This is obtained by adjusting the frequency produced by the synthesiser included in the microwave excitation signal generator. Such adjustments amount to attributing different values to the factor $K _ { s }$ introduced in Section 6.4.1c for different clocks of the same make. This operation requires calibration with respect to some reference source. The notion of accuracy thus has no meaning as far as the rubidium cell clock is concerned.

# (c) Long term frequency instability and the effect of environmental conditions

In the long term, for $\tau$ greater than $1 0 ^ { 3 } – 1 0 ^ { 4 }$ s, the frequency of a rubidium cell clock drifts by $1 - 5 \times 1 0 ^ { - 1 1 }$ per month.Thereasonsarenotyet perfectly understood. It is probably related to chemical reactivity between rubidium and glass,and changes in the buffer gas composition and pressure caused by diffusion through the filter and cell walls.

The rubidium standard is the most sensitive of allatomic time and frequency standards to environmental conditions [6.95]. Effects of temperature variations are amongst the most important,amounting to $1 0 ^ { - 1 0 } \mathrm { p e r } ^ { \circ } \mathrm { C } .$ Temperature variations affect the light spectrum emitted by the lamp as wellas the efficiency of the ensuing hyperfine filtering,and hence the light shift. They also change the probability of collisions between rubidium atoms and buffer gas molecules in the resonance cell,thereby affecting the associated shift in the hyperfine transition frequency.

Technical choices with regard to composition and pressure of the gas used, as wllas the temperatures assigned tothe lamp,thehyperfineflter(if separate)and the resonance cell,are largely determined by the need to minimise the effects of environmental conditions. Despite the difficulties involved, rubidium clocks showing very low sensitivity to ambient conditions have been produced.Theyare carred on board satellites of the Global Positioning System (GPS) (see Section 9.2.2),side by side with caesium clocks.

# 6.6.5 Current studies and prospects

Theoretical and experimental work has shown that the discharge lamp could usefully be replaced by a semiconducting laser emitting at $7 8 0 ~ \mathrm { n m }$ [6.96, 6.97, 6.98]. This type of laser is commonly used in CD players and hence cheap to produce. The quasi-monochromatic light of the laser is stabilised on the rubidium $\mathbf { D } _ { 2 }$ line,and very efficient optical pumping is possible for a much lower flux than is required when a lamp is used. The relative height of the resonance is increased whilst the total current output by the photocellfalls. As aconsequence,the potential medium term frequency stability is of the order of $1 0 ^ { - 1 3 } \tau ^ { - 1 / 2 }$ Itisalsot this promises to improve long term frequency stability.

Laboratory studies have produced rubidium 87 masers operating in active mode [6.99,6.10o]. To this end, the production of a population inversion between levels $F = 2$ ， $m _ { F } = 0$ and $F = 1$ ， $m _ { F } = 0$ was optimised,as far as such is posible,and the resonance cell placed in acavity with the best quality factor that could be attained. The main attraction of a rubidium maser is its excellent frequencystability,of theorderof $1 0 ^ { - 1 3 }$ , for sampling periods $\tau$ close to $1 \mathrm { ~ s ~ }$ However,thisstabilitytends todiminish for $\tau > 1 \mathrm { ~ s ~ }$ ,owing to the light shift and the shift caused by collisions with the bufer gas.

# 6.7 Stored ion clocks

It has been known for several decades that ions can be confined in vacuum by means of electromagnetic fields. This confinement means that the ions are held withina limited volume of space,without the help ofmaterial walls,for periods of time as long as one day or more.

In a Penning trap, static electric and magnetic fields are used, whilst in a Paul trap,the feld is a radiofrequency electric field. In practice,the presence of a magnetic field,as in the Penning trap,is not anadvantage for the applications we have in mind here.We shall therefore restrict discussion to confinement by the Paul trap [6.101].

Many ions exhibit a hyperfine structure. Indeed,for the following ions,for example, the hyperfine splitting in the ground state is known to better than one part in $1 0 ^ { 8 }$ ： $^ 3 \mathrm { H e } ^ { + }$ ， $^ { 9 } \mathrm { { B e } ^ { + } }$ ， $^ { 2 5 } \mathrm { M g ^ { + } }$ ， $^ { 8 8 } \mathrm { S r ^ { + } }$ ， $^ { 1 1 3 } { \mathrm { C d } } ^ { + }$ $^ { 1 3 5 } \mathrm { { B a } ^ { + } }$ ， $^ { 1 3 7 } \mathrm { { B a } ^ { + } }$ $^ { 1 7 1 } { \mathrm { Y b } } ^ { + }$ ， $^ { 1 7 3 } { \mathrm { C d } } ^ { + }$ and $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ . In 2000, only the $^ { 1 7 1 } { \mathrm { Y b } } ^ { + }$ and $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ions had been used to build instruments that could be considered as atomic time and frequency standards. Since there are thus far more results for mercury ions,we shall concentrate on mercury ion standards, with confinement in a Paul trap. The original idea was put forward by Major at the end of the 196Os,in the NASA laboratories. The hyperfine resonance of confined $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ions was first observed experimentally at NASA [6.1O2] and subsequently at the University of Mainz (Germany) [6.103].

The main steps in developing the corresponding frequency standard were carried out at the Laboratoire de l'horloge atomique (France) [6.104], Hewlet-Packard (USA) [6.105, 6.106], and the Jet Propulsion Laboratory (USA) [6.107, 6.108, 6.109]. These instruments can be made small enough for use in the field. Frequency instabilities below $1 0 ^ { - 1 3 } \tau ^ { - 1 / 2 }$ have been achieved. More recently, a laser-cooled mercury ion frequency standard has been successfully operated at the National Institute of Standards and Technology (USA),showing a relative frequency instability of $3 . 3 \times 1 0 ^ { - 1 3 } \tau ^ { - 1 / 2 }$ and an inaccuracy of $3 \times 1 0 ^ { - 1 5 }$ [6.110]. This is a more complex and bulky device.

We shall begin by giving the principle of ion confinement in a Paul trap. We then go on to describe the mercury ion frequency standard using a cloud of ions that are thermalised by collision with an inert gas at room temperature and optically pumped by means of an isotopic lamp. We shall briefly discuss the ytterbium ion frequency standard and close by presenting the laser-cooling of ions and the particularities of the laser-cooled mercury ion frequency standard.

# 6.7.1 Confining ions in a radiofrequency trap

(a) Potential distributions

We begin by considering the two potential distributions used to confine charged particles.They correspond to the linear trap (also used in some gas analysers) and thethree-dimensional trap,respectively.

Two-dimensional quadrupole field. The potential distribution described in Cartesian coordinates $( x , y , z )$ by

$$
V ( x , z ) = C ( x ^ { 2 } - z ^ { 2 } )
$$

can be realised physically since theLaplacian of this potential is indeed zero. The quantity C is a constant. The potential is zero on the y axis. In the (x, z) plane,theequipotential curves arerectangular hyperbolas.

If we introduce conducting electrodes that follow these equipotentials, and raise them tothe corresponding potential,the potential distribution desribed by (6.129)can be created at every point between the electrodes.In particular,if the turningpointsof the electrodesareequidistant from the $y$ axis,the configuration shown in Figure 6.33a is obtained, with

![](images/73b8d3427f627278ae6d06c24d0610d9a6e57ed734296b778083ffe6e0ed61fd.jpg)  
Fig.6.33. Linear trap (in two dimensions). (a) Equipotentials viewed in a transverse plane. (b) Electrode structure.

$$
C = \frac { V _ { 0 } } { x _ { 0 } ^ { 2 } } = \frac { V _ { 0 } } { z _ { 0 } ^ { 2 } } ,
$$

where $V _ { 0 }$ is the absolute value of the potential to which the electrodes are raised and $x _ { 0 } = z _ { 0 }$ is the distance separating the turning points of the electrodes from the $y$ axis.

The components of the electric field between the electrodes are

$$
E _ { x } = - \frac { 2 V _ { 0 } } { z _ { 0 } ^ { 2 } } x \ , E _ { y } = 0 \ , E _ { z } = \frac { 2 V _ { 0 } } { z _ { 0 } ^ { 2 } } z \ .
$$

In practice, the electrodes cannot extend infinitely along the asymptotes of the hyperbolas. They are therefore truncated,as shown in Figure 6.33b. To simplify the construction, they are usually reduced to simple rods of circular cross section. It is then shown that, near the neutral axis,where the ions are in fact confined, the potential distribution tends to the one given by (6.129).

Three-dimensional quadrupole field. The following potential distribution, expressed in cylindrical coordinates,

$$
V ( r , z ) = C ( r ^ { 2 } - 2 z ^ { 2 } ) ,
$$

![](images/c728388d5899ed31c130149ff4dce4a7659a8265e31e9c314e449d11208cf7de.jpg)  
Fig. 6.34. Three-dimensional trap. (a) Equipotentials viewed in a meridian plane. (b) Electrode structure.

can also be realised physically. This potential is zero at the origin and the equipotentials are hyperboloids of revolution about the $z$ axis. The latter comprise a ring-shaped surface centred on the z axis and two other surfaces cut by the $z$ axis,which might be viewed as a kind of lid. The ring component, with minimum distance $r _ { 0 }$ from the $z$ axis,and the lids with turning points at distance $z _ { 0 } = r _ { 0 } / \sqrt { 2 }$ from the centre, have the same absolute value of the potential. If these equipotentials are replaced by material electrodes brought to the potential $V$ with $| V | = V _ { 0 }$ ,we obtain the configuration with

$$
C = \frac { V _ { 0 } } { r _ { 0 } ^ { 2 } } = \frac { V _ { 0 } } { 2 z _ { 0 } ^ { 2 } } \ ,
$$

as illustrated in Figure 6.34a.

The components of the electric field between the electrodes are

$$
E _ { r } = - \frac { V _ { 0 } } { z _ { 0 } ^ { 2 } } r , \quad E _ { z } = 2 \frac { V _ { 0 } } { z _ { 0 } ^ { 2 } } z .
$$

As in the previous case, the electrodes are actually finite. In practice, they are made as shown schematically in Figure 6.34b. For the sake of convenience, they may not have exactly the theoretical hyperboloid shape. However, close to the centre, the potential is adequately described by (6.132).

# (b) Confinement of charged particles

Equations (6.131) and (6.134) show that the orthogonal components of the electric field are proportional to the distance from the axis of the linear trap, or to the centre of the three-dimensional trap, but with opposite signs. If the applied potential diference is constant,a charged particle willtherefore be subjected to a force with one component tending to restore it towards the axis or the centre,and one component tending to dispel it from the trap.

![](images/7903543ee95e8530e13158bfc1eedc12fded5734e50e57ca03466ae165518089.jpg)  
Fig. 6.35. Origin of the restoring force,bringing ions back towards the axis in alinear trap.

However, confinement can be achieved if the applied potential difference alternates.The particle motion can,of course,be describedanalytically via the fundamental equation of dynamics. We thus obtain two Mathieu differential equations. Their solutions are stable for certain values of parameters defined in terms of the amplitude and frequency of the potential difference applied across the electrodes, the trap dimensions $r _ { 0 }$ and $z _ { 0 }$ ,and the mass and charge of the particle. In this case, the particle oscillates about the axis or the centre, without reaching the walls.Confinement is thus physically realised.A complete study of the motion of the ions shows that stability conditions are optimised if the applied potential difference includes a d.c. component [6.101].

In the following, we present a simple qualitative argument to explain the origin of the restoring force that confines the ions in both directions.

Considera linear trap and, without loss of generality,imagine thata positive ion is placed in it.The electric field forces the ion intoa low amplitude sinusoidal motion called the micromotion. It has the same frequency as the electric field,but it is completely out of phase with it.Figure6.35 shows the time variation of the electric field at two points in the $( x , z )$ plane located on the $x$ and axis,with coordinates (x1 > 0, O) and (O, z1 > O),respectively. The electric fields there are out of phase since, by (6.131), $E _ { x }$ and $E _ { z }$ have opposite signs. The micromotion executed locally by the ion is also shown. This motion allows it to explore the electric field. However, the latter is non-uniform,being proportional to the distance from the axis,and the electrical force on the ion lis thereby distorted,as shown in the figure. Consequently, the average value of the force is not zero and we observe that it is directed towards the axis. This restoring effect on the ion forces it into a two-dimensional transverse harmonic motion about the trap axis.This is called the macromotion or secular motion.It has a low frequency compared with the electric field itself. Longitudinal confinement is arranged by the end electrodes, positioned on the axis and held at a constant repulsive potential.

By a similar explanation, it can be shown that, in a three-dimensional trap, confinement is obtained in the axial direction and in every radial direction. In this case,confinement is indeed three-dimensional.

Applying a potential difference with an alternating component across the electrodes of a linear or three-dimensional trap,ions can be confined in the vicinity of the axis or centre, respectively. The ions are suspended in the vacuum under the effects of forces of electrical origin that bind them with respect to the trap electrodes. They follow an extensive secular motion, on which is superposed a higher frequency but lower amplitude micromotion. For a trap in which the electrode spacing is of the order of one centimetre,and the applied alternating potential difference has frequency around $1 0 0 ~ \mathrm { k H z }$ and amplitude around $1 0 0 \mathrm { V } ,$ the frequency of the secular motion is of the order of $\mathrm { { 1 0 } k H z }$ in the case of mercury ions,and the amplitude is less than the internal dimensions of the trap.

By their almost harmonic motion, the ions behave as though they were moving in a parabolic potential well with depth of the order of $1 0 \mathrm { V }$

# 6.7.2 Confinement of a cloud of ions

(a) Ion cloud density

The density of the ion cloud that can be confined in this way is extremely low, due to repulsive electrostatic forces between the charged particles. This density is of the order of 10 ions cm-3, corresponding to a partial pressure in the region of 10-8 Pa.comparable with that of the residual gases in an extremely high vacuum. The ionic medium is thus very dilute and collision interactions scarce.

![](images/fd9474091d35e6e1fa9dafeadff98905cdfcc57c59b226181a936b635c1e280e.jpg)  
Fig. 6.36. Schematic illustration of the absorption spectrum of an ion confined in a radiofrequency trap.

# (b)Absorption spectrum of the ions

When the ions are irradiated by an electromagnetic wave of fixed frequency $\nu$ ,they feel a frequency modulated wave. This is due to their own motion and the associated Doppler effect. The spectrum of the signal received by the ions thus includes a carrier at frequency $\nu$ and lateral lines at frequencies $\nu \pm n f _ { \mu }$ and $\nu \pm m f _ { \mu ^ { \prime } }$ ,where $n$ and $m$ are integers and $f _ { \mu }$ ， $f _ { \mu ^ { \prime } }$ are the secular motion and micromotion frequencies,respectively.Inaddition,the ions exbita very sharp hyperfine resonance,due to the fact that confinement times can be extremely long. Its width is much less than $f _ { \mu }$ and hence also $f _ { \mu ^ { \prime } }$ If the frequency $\nu$ is varied,the ions tend to absorb the incident radiation each time one of the spectral components coincides,up to the width of the resonance, with the hyperfine resonance frequency $\nu _ { 0 }$

Switchingfromthestandpointoftheionstothatoftheoserver,everyhing happens as though the ionic absorption (or emission) spectrum were composed of very narrow lines at frequencies $\nu _ { 0 } \pm n f _ { \mu }$ and $\nu _ { 0 } \pm m f _ { \mu ^ { \prime } } .$ The spectrum is shown schematically in Figure 6.36.

When the radiation frequency $\nu$ is very close to the hyperfine transition frequency $\nu _ { 0 }$ ,the lateral lines are not excited and everything happens as though the Doppler effect were inoperative. This result has already been mentioned in Section 6.2.3. It can be shown that the Dicke condition (6.15), limiting the dimensions of the region occupied by the ions,implies that the central component of the absorption spectrum should be barely attenuated and that the lateral components should be of low amplitude.

# (c) Ion energies

The resonance signal that can be obtained from a group of ions or atoms is proportional to the number of particles that can be observed. Efforts are therefore made to increase this number,insofaras thisispossible.However,in the case of ions, there isa correlation between the number of ions confined and theirkinetic energy. The latter is an increasing function of this number. The same is therefore true of the second order Doppler frequency shift given by (6.16).

It is easy to find a qualitative explanation for this coupling. Because of Coulomb repulsion, the ionic cloud occupies an ever greater volume as the number of ions increases. Since the electric force acting on the ions is proportional to their distance from the trap axis or centre (by (6.131) and (6.134)), their kinetic energy increases. For the three-dimensional trap, the average kinetic energy is around $2 \ \mathrm { e V } .$ Despite the large mass of the mercury ion, this leads to a second order Doppler frequency shift of the order of -10-11.

The kinetic energy of the ions is reduced by introducing helium gas at very low pressure, of the order of $1 0 ^ { - 3 }$ Pa, so as not to cause a further frequency shift that might actually worsen the situation. The average kinetic energy of this gas is $4 \times 1 0 ^ { - 2 } \ \mathrm { e V }$ at room temperature. This collisional cooling method is not very effective in practice. The second order Doppler shift can be reduced to -5 × 10-12.

The situation is better in a linear trap because the ions spread out over a cylindrical region about the trap axis.For a given number of ions, the transverse extent of the cloud can be decreased if the cylinder length is greater than its diameter. The average kinetic energy is thereby diminished [6.1O7,6.108,6.109]. Using helium gas at a partial pressure of $1 0 ^ { - 3 }$ Pa, the second order Doppler shift falls to around $- 1 0 ^ { - 1 2 }$ It canalsobeshownthat,inalineartrap,theaverage kinetic energy is lesssensitive tofluctuations in the a.c.potential difference applied across the electrodes.

These advantages explain the current preference for using linear traps in confined mercury ion frequency standards.

# 6.7.3 Description of a frequency standard using a cloud of mercury ions

# (a) Spectroscopic properties of $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$

The nuclear spin of the 199 isotope of mercury is $1 / 2$ . In addition, when the $\mathrm { H g ^ { + } }$ is produced by removing an electron from the outer electron shell, it has an electronic structure very similar to the alkali metals, with an unpaired electron on the outermost electron shell.

The $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ion therefore has a ground state hyperfine structure as simpleas the hydrogen atom itself, with just four hyperfine sublevels,viz., $F ~ = ~ 0$ $m _ { F } = 0$ and $F ~ = ~ 1$ ， $m _ { F } = - 1 ,$ 0,1. The proportionof levels useful for operating a frequency standard, i.e., the levels (O, O) and (1,0), is therefore as large as possible. This makes it easier to observe the hyperfine resonance signal ofalimited number of ions.Note also that the hyperfine spliting is large, corresponding to about $4 0 . 5 \ : \mathrm { G H z }$ . For a given hyperfine resonance width, the quality factor of this resonance will thus be higher than for the atoms considered previously. This same property also favours frequency stability.

(b) Optical pumping of $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ and observationofthe hyperfine resonance

The hyperfine states of an ion cannot be separated by magnetic selection because the deflecting force associated with the electrical charge is far greater than that arising from the magnetic moment of the unpaired electron. State selection must therefore be carried out byoptical pumping.

In the present case, there is a fortunate isotopic coincidence between the absorption spectrum of $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ and the emission spectrum of $^ { 2 0 2 } \mathrm { H g } ^ { + }$ .The later spectrum is emited by alamp containing the202 isotope of mercury and excited by aradiofrequency discharge. This isotope has no hyperfine structure and it just happens that the wavelength of the $\mathrm { D } _ { 1 }$ line of $^ { 2 0 2 } \mathrm { H g ^ { + } }$ ,near $1 9 4 ~ \mathrm { { n m } }$ lies very close to the wavelength of the transition between the $F = 1$ hyperfine level of the $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ground state $^ 2 S _ { 1 / 2 }$ and its first excited state ${ } ^ { 2 } \mathrm { P } _ { 1 / 2 }$ The situation is thus very similar to the one illustratedin Figure 6.4a,except that the incident light excites ions in level $\beta$ (here, the $F = 1$ level) and optical pumping populates level $\alpha$ (here, the $F = 0$ level).

Fluorescence light emitted by ions when they spontaneously decay from the first excited level down to the ground state is not very intense because the population of the $F = 1$ level is reduced. If the ions are now iradiated by an electromagnetic wave with frequency close to the hyperfine transition frequency, the $F = 1$ level repopulates and the fluorescence light at $1 9 4 ~ \mathrm { n m }$ intensifies. Its intensity is measured and, when the applied signal frequency sweepsacross the hyperfine transition frequency $\nu _ { 0 }$ ,aresonance curve is obtained with a maximum at that frequency.

If optical pumping were accomplished using monochromatic light, it would be more efficient and the resonance would be more intense. However, at the time of writing (2ooO),there is no far ultraviolet continuous-wave laser. Coherent radiation has been produced at wavelengths as short as $1 9 4 ~ \mathrm { n m }$ using optical frequency synthesis techniques,i.e.,by multiplying and mixing frequencies in non-linear crystals [6.111]. The experimental setup is complex and costly, so the $^ { 2 0 2 } \mathrm { H g ^ { + } }$ lamp is still used in relatively compact devices.

# (c) Experimental setup and resonance curve

The experimental setup, designed by the Jet Propulsion Laboratory (USA), is shown schematically in Figure 6.37.

![](images/1b7336412a30b06092667aee6f37cc5ecc045ae5213416af67f4efac684377ce.jpg)  
Fig.6.37. Confined mercuryionresonator. (a)Usefulpartofthe $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ spectrum. (b) Simplified representation of the confined mercury ion resonator. Fluorescence light is observed at right angles to the plane of the figure.

A neutral mercury 199 vapour is introduced in a controlled manner, at very low pressure,by heating mercury oxide. The vapour encounters a blast of electrons from an electron gun. The ions thereby produced are confined by applying a suitable potential difference to the linear trap electrodes. The latter consist of four regularly spaced cylindrical rods,about 1 cm apart. Helium gas at a pressure of about $1 0 ^ { - 3 }$ Pa reduces the kinetic energy of the ions.

Light from the $^ { 2 0 2 } \mathrm { H g } ^ { + }$ lamp is directed towards the ion cloud. After crossing the trap, it is collected in a light trap in order to reduce the intensity of spurious light that might impede observation of fluorescence light from the ions. The fluorescence light is focused onto a photomultiplier, in a direction perpendicular to the plane of the figure.

The microwave interrogation signal at $4 0 . 5 \mathrm { G H z }$ is applied using a horn. The electromagnetic wave propagates at right angles to the trap axis.

Magnetic shielding attenuates the Earth's magnetic field and its fluctuations. It contains coils creating a uniform and stable magnetic field, with strength similar to that in a caesium beam clock. A high vacuum pump and various other devices are incorporated.

The resonance is observed with the help of Ramsey's method. In this case, however, the two successive interactions do not result from motion of the atoms (orions),asin $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ frequencystandard,to cessive interactions are obtained by pulsing the oscillating field. During an observation sequence, this field irradiates the region occupied by the ions for twobrief instants separated bya time interval $T$ . The Ramsey method therefore operates in the time dimension here.

![](images/fa8e0669d0f2fbeac25cc22d0108fbd475f33d0409552fea805d15882641ef1c.jpg)  
Fig. 6.38. Response of a linear mercury ion trap.The frequency origin is positioned at the ground state hyperfine transition frequency.From [6.10,6.108,6.109].

An observation sequence typically begins by reloading the trap in order to maintain the number of ions (and hence their energy) at a constant level from one cycle to the next. The electron gun is therefore activated briefly. The lamp is then lit for about $1 . 5 \mathrm { ~ s ~ }$ ,by which time the ions have been prepared in the state $F = 0 .$ The microwave radiation is applied for two time intervals $\tau$ lasting about $0 . 3 \ : \mathrm { s }$ ,separated bya time $T$ ,anywhere between 2 and $3 0 \mathrm { s }$ ,during which irradiation ceases. The lamp is subsequently relit and the fluorescence light intensity measured,todiscover the effect that the microwave radiation has had. Figure 6.38 shows the resonance curve thus obtained, with $T = 2 . 5 ~ \mathrm { s }$ [6.107, 6.108,6.109]. It represents the transition probability as described by (6.43).

The quality factor $Q \mathrm { { a } } \mathfrak { t }$ of the central fringe of the resonance curve in Figure 6.38 is $2 \times 1 0 ^ { 1 1 } .$ It can be increased,inpropti to $T$ . As a general rule, the temporal Ramsey method applied to confined ions is currently the method of high resolution spectroscopy that produces the highest quality factors for atomic resonances.

# (d) Controlling the frequency of an oscillator

The response of the atomic system can only be observed at discrete times, at the end of an interrogation sequence. The frequency of a quartz oscillator is thus controlled by the ionic hyperfine resonance in the same way as it would be by a cold caesium atom fountain.

# 6.7.4 Metrological properties of frequency standards using a cloud of mercury ions

# (a) Medium term frequency instability

When sampling periods are long compared with the time constant for servo control of the local oscillator,and hence longer than $T$ , the medium term frequency instability of the confined ion frequency standard is characterised by (6.86).

Detection noise arises from shot noise in the detected light flux. There are two components in the detected flux, viz.,fluorescence light from ions and light produced by unwanted reflection of the incident light. In practice the latter is more intense than the fluorescence light. This introduces an inordinately large shot noise. However, the high value of the quality factor $\mathcal { Q } _ { \mathrm { a t } }$ favours frequency Stability.AnAllandeviationof $7 \times 1 0 ^ { - 1 4 } \tau ^ { - 1 / 2 }$ has beenobtained,puttingthe mercury ion standard into the ranks of the most stable,as can be seen from Figure 6.11 [6.107, 6.108, 6.109].

# (b) Residual frequency shifts

The main frequency shifts affecting the mercury ion frequency standard come from the quadratic Zeman effect, the second order Doppler efect,and coli-sions with the helium buffer gas.

The static magneticfeld is typically $3 . 5 \times 1 0 ^ { - 6 }$ T. The shift in the hyperfine transition frequency of the $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ground state is then equal to $3 \times 1 0 ^ { - 1 2 }$ It is much smaller than in a caesium beam clock, where it would have a value around 1.7 × 10-10.

The second order Doppler shift and the shift due to collisions with the bufer gas are related since it is the density of the buffer gas that determines the kinetic energyoftheions.Foraheliumpartialpressreof $1 0 ^ { - 3 }$ Pa, the frequency shift due to these two associated effects is close to $1 0 ^ { - 1 2 }$

Note that the shift arising from the quadratic Stark effect in the presence of the confining electric field is as low as a few times $1 0 ^ { - 1 4 }$

# (c) Long term frequency instability and inaccuracy

The long term frequency instability depends on the sensitivity of the observed transition frequency to environmental conditions and operating parameters. These instabilities may arise from fluctuations in the surrounding magnetic field,the potential difference across the electrodes,the number of confined ions,and the temperature and pressure of the buffer gas.

Experience shows that these parameters can be sufficiently well controlled to ensure a frequency instability of the order of $1 0 ^ { - 1 5 }$ for $1 0 ^ { 4 } < \tau < 1 0 ^ { 6 } \ s$ [6.107, 6.108, 6.109].

Theoretical and experimental analyses of the various frequency shifts provide an estimate of a few times $1 0 ^ { - 1 3 }$ for the inaccuracy of the confined $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ioniedd

# 6.7.5 Ytterbium ion frequency standard

The ion $^ { 1 7 1 } { \mathrm { Y b } } ^ { + }$ has been used to make a confined ion frequency standard. Its nuclear spin is also $1 / 2$ ,and its hyperfine transition frequency in the ground state is close to $1 2 . 6 \ \mathrm { G H z }$ Optical pumping is carried out on the $\mathrm { D } _ { 1 }$ line at $3 6 9 . 5 ~ \mathrm { n m }$ .Standards have been constructed in different ways.In one case,the radiofrequency trap is three-dimensional and the light source provided by a dye laser with doubled frequency [6.112]. In another case, the radiofrequency trap is linear and the pumping light obtained from a titanium-sapphire laser [6.113].

The measured frequency instabityisclose to $1 0 ^ { - 1 3 } \tau ^ { - 1 / 2 }$ for $1 0 0 < \tau <$ $3 0 0 0 \ s$

The ground state hyperfine transition frequency for $^ { 1 7 1 } { \mathrm { Y b } } ^ { + }$ has been measured to within 2 mHz [6.113].

# 6.7.6 Laser-cooled mercury ion frequency standard

Ions can be cooled by laser irradiation in the same way as atoms [6.114]. In fact,the experimental method is simpler for ions than for atoms because they are held close to the trap centre or axis. The first radiative cooling of confined ionswas accomplished in 1978 at the National Bureau of Standards, since renamed the National Institute of Science and Technology (NIST).

The cooling mechanism can be understood intuitively. The optical absorption spectrum of a confined ion has lateral lines due to the periodic component of its motion,in exactly the same way as its microwave absorption spectrum, shown in Figure6.36. The ioncan therefore absorb a photon when illuminated by a laser beam with frequency lower than the optical transition frequency. By fluorescence, it then emits a photon whose mean frequency is equal to the optical transition frequency. Each absorption-fluorescence cycle thereby removes energy from the kinetic energy of the ion.A single laser suffices to achieve this result,and residual thermal energies corresponding to a temperature of about $1 0 \mathrm { m K }$ are commonly obtained. The second order Doppler shift is then reduced to a completely negligible level,of the order of1o-17or10-18.

Such low temperatures can only be attained if the number of confined ions is small. They are then localised very close to the trap axis where they form a linear crystal of a few ions. Since the ions lie along the nodal line of the radiofrequency field, the second order Stark effect becomes negligible. Unfortunately, frequency stability is reduced by the small number of ions. This is counterbalanced by a reduction in the hyperfine resonance line width, thanks to an increase of up to $1 0 0 \mathrm { s }$ in the Ramsey interaction time $T$ . The frequency shift due to collisions with residual gases must be reduced as far as possible by rarefaction,and this requires the use of cryogenic techniques.

A laser-cooled mercury ion frequency standard has been built and operated at NIST according to the principles just described [6.11O]. Coherent radiation is produced at $1 9 4 ~ \mathrm { n m }$ by optical frequency synthesis [6.111]. It is used to cool the ions and also to create a population difference between the hyperfine sublevels. Ions are stored in a $4 ~ \mathrm { m m }$ long linear radiofrequency trap with an electrode separation close to $1 \ \mathrm { m m }$ . Under the reported operating conditions, a set of seven cooled ions form a linear crystal along the trap axis. The trap is placed in an enclosure cooled to the temperature of liquid helium. The clock transition is probed using the Ramsey technique in the time domain. During one elementary cycle of operation, the ions are first cooled for $3 0 0 ~ \mathrm { { m s } }$ They are then optically pumped in the $F = 0$ ， $m _ { F } = 0$ level of the ground state. The light is switched off and the Ramsey microwave interrogation is accomplished. For this purpose, two $4 0 . 5 \dots \mathrm { G H z }$ pulses of duration $2 5 0 ~ \mathrm { { m s } }$ are applied with a separation of up to $1 0 0 \mathrm { s } .$ The clock transition is then detected optically. The frequency control of the quartz crystal oscillator is very similar to that implemented in atomic fountains. The frequency instability and inaccuracy achieved are $3 . 3 \times 1 0 ^ { - 1 3 } \tau ^ { - 1 / 2 }$ and $3 . 5 \times 1 0 ^ { - 1 5 }$ speciely mance is expected by increasing the number of stored ions or by preparing the ions in special quantum states [6.115, 6.116].

# 6.8 Other atomic frequency standards

Hyperfine structure transitions have no exclusive claimas atomic frequency references. Other transitions may be acceptable, provided they have the required qualities.

# 6.8.1 Magnesium beam frequency standard

The alkaline earth atoms have no hyperfine structure in the ground state. However,there are interesting transitions betweenlevels of their excited states.For example,in magnesium, the frequency of one of these transitions is $6 0 1 ~ \mathrm { G H z }$ and the lifetime of the Ievels is such that the quality factoris close to $1 0 ^ { 1 0 }$ A beam frequency standard has been built on the basis of this transition and results are encouraging [6.117]. A more efficient preparation of the relevant atomic states, together with cooling of the magnesium atoms, would be required to improve this device.

# 6.8.2 Optical frequency standards

A great many frequency standards have been constructed, or are under development, in the optical region of the spectrum. They use atomic or molecular transitions between the ground state and an excited state, or between two excited states.The light source used to observe such a transition is always a laser, with frequency controlled by the frequency of the selected transition. These are therefore passive frequency standards.The references are transitions in the following molecules,atoms and ions,e.g, $\mathrm { I } _ { 2 }$ ， $\mathrm { C H } _ { 4 }$ ， $\mathrm { C O } _ { 2 }$ ， $\mathrm { O s O } _ { 4 }$ ,Rb,Ca, $\mathrm { H g ^ { + } }$ ， ${ \mathrm { Y b } } ^ { + }$ ， $\mathrm { B a ^ { + } }$ ， ${ \mathrm { S r } } ^ { + }$ ， $\mathrm { C a ^ { + } }$ ， $\mathrm { I n ^ { + } }$ .The whole available range of CW lasers is concerned here, including $_ \mathrm { H e - N e }$ ， $\mathrm { C O } _ { 2 }$ ,semiconductor, neodymium-doped YAG, titanium-sapphire,and so on.

Remarkable results have been obtained. At frequency 29 THz $( 1 0 ~ \mu \mathrm { m } )$ ,the $\mathrm { C O } _ { 2 }$ laser stabilised on a transition of the osmium tetroxide molecule $\mathrm { O s O } _ { 4 }$ has a frequency instability below $1 0 ^ { - 1 4 }$ for $1 0 \mathrm { ~ s ~ } < \tau < 1 0 ^ { 4 }$ s, a long term (1 yr) reproducibility of $1 . 3 \times 1 0 ^ { - 1 3 }$ ,anda potentialinaccuracyof theoder of $1 0 ^ { - 1 4 }$ [6.118]. Similar results have been obtained at 88 THz $( 3 . 3 9 \mu \mathrm { m } )$ with the He-Ne laser stabilised on a transition of the methane molecule [6.119].

# 6.8.3 Optical frequency standards based on individual ions at rest

The ion confinement technique is likely to play a key role in the development of extremely high performance optical frequency standards. Indeed, in 1973, Dehmelt put forward the idea of using a single ion at rest [6.120].

Consider an ion in which two transitions with very different properties can be identified. One couples the ground state to a level of very short lifetime,of the order of $1 0 ~ \mathrm { n s }$ .This means that about $1 0 ^ { 8 }$ absorption-fluorescence cycles can be carried out per second and the ion can thus be very efficiently cooled. The other transition is associated with a very low probability. It connects the ground state to a metastable state with a lifetime of about 1 s. The corresponding resonance therefore exhibits an intrinsic width of the order of 1 Hz. It constitutes the optical reference frequency with a quality factor somewhere between $1 0 ^ { 1 4 }$ and $1 0 ^ { 1 5 }$ . Since the cooling transition provides something like $1 0 ^ { 8 }$ fluorescence photons per second, the presence of a single ion in the trap is easy to detect. Indeed, this has been demonstrated experimentally in several laboratories.

![](images/14f7ba95d4fbdf4fac094123206b4da97a7f7ed8be2a7f69ff4ba5a5f1ec1e18.jpg)  
Fig. 6.39. Energy levels in the indium ion chosen to build an optical atomic frequency standard.

A single cold ion resides on the axis of a linear Paul trap, with an extremely low kinetic energy. We thus achieve a good approximation to the idea of a single atom (or ion) at rest. In such a situation,the causes of unwanted frequency shifts are reduced to an absolute minimum.

The possibility of using the indium ion $^ { 1 1 5 } \mathrm { { I n } ^ { + } }$ has been considered [6.121, 6.122]. The relevant energy levels are shown in Figure 6.39. The ${ } ^ { 3 } \mathrm { P } _ { 0 }$ level is the one with a long lifetime. This ion has no electron angular momentum in the ground state ${ } ^ { 1 } \mathrm { S } _ { 0 }$ , nor in the metastable state ${ } ^ { 3 } \mathrm { P } _ { 0 }$ . Hence, the Zeeman frequency shift is extremely smal.Moreover, the reference transition frequency is not shifted by the Stark effect,and it is in factcompletely immune to the presence of a confining electric field. The production of two emissions at 231 and $2 3 6 ~ \mathrm { n m }$ appears feasible by twice doubling the emission frequency of semiconductor lasers.

The reference transition can be detected by the so-called shelving method, which works as follows [6.12O]. If the ion is in the ground state ${ } ^ { 1 } \mathrm { S } _ { 0 }$ ,it is detected as a result of the $2 3 1 ~ \mathrm { { n m } }$ fluorescence light released after irradiation by the cooling light beam. On the other hand,if the frequency of the radiation at $2 3 6 ~ \mathrm { { n m } }$ is tuned to the reference transition frequency,the ion is carried into the state ${ } ^ { 3 } \mathrm { P } _ { 0 }$ ,and the fluorescence light disappears.

An excellent frequency stability is expected of this frequency standard, becauseof the high valueof the quality factorand the high signal-to-noiseratio for detecting the transition. The inaccuracy may be as small as $1 0 ^ { - 1 7 }$ ,because the frequency shifts affecting the reference transition are significantly reduced.

Convincing experimental results have beenobtainedrecentlyat NISTusing a single laser-cooled $^ { 1 9 9 } { \mathrm { H g } } ^ { + }$ ionstoredinacrogniclinearradiofrequency trap[6.123].Ion cooling is achieved by inducing transitionsat $1 9 4 \mathrm { n m }$ between the $^ 2 S _ { 1 / 2 }$ ground state and the short-lived ${ } ^ { 2 } \mathrm { P } _ { 1 / 2 }$ first excited state. The $2 8 2 \mathrm { n m }$ referencetransitionoccursbetweenthegroundstateandthemetastable ${ } ^ { 2 } \mathrm { D } _ { 5 / 2 }$ state having a lifetime of $9 0 ~ \mathrm { m s }$ .The shelving method is implemented and the detection of the $2 8 2 ~ \mathrm { n m }$ transition is accomplished by observing the fluorescence light at $1 9 4 ~ \mathrm { n m }$ . A line width of $6 . 7 \ \mathrm { H z }$ for the $2 8 2 ~ \mathrm { n m }$ transition $( 1 . 0 6 \times 1 0 ^ { 1 5 } ~ \mathrm { H z } )$ has been observed.Thecorresponding line quality factoris equal to $1 . 6 \times 1 0 ^ { 1 4 }$ . It is the highest ever achieved in microwave and optical spectroscopy. This result proves the true potentiality of optical frequency standards to compete successfully with frequency standards based on microwave transitions.

It should be noted, however, that in order to observe a resonance in the optical region with width as small as $1 \ \mathrm { H z }$ ,the light source itself must have a spectral width well below this value. Specific studies will be needed to construct such a source.

# 6.8.4 Optical frequency standards for time measurements

The frequency of radiation at a wavelength of $0 . 6 ~ \mu \mathrm { m }$ ，for example, is $5 0 0 \times 1 0 ^ { 1 2 } \ \mathrm { H z }$ .This is about 50oo times higher than frequencies in the most advanced systems $( \sim ~ 1 0 0 ~ \mathrm { G H z } )$ ),used for telecommunications and radar detection. Although several specialised laboratories are able to compare the frequencies of a microwave signal and those of an optical signal, using the frequency synthesis technique,the experimental setups are delicate,cumbersome and costly. At the time of writing,no practical way has yet been discovered for using optical frequency standards to produce a reliable and durable time scale.

Research is in progress with regard to improving this situation. New results have opened the way to much easier comparisons of frequencies in the microwave and optical domains [6.124,6.125]. They have been obtained using a mode-locked laser which regularly emits very narrow (a few femtoseconds) and intense pulses. This periodic radiation creates a frequency comb in the optical domain. The repetition frequency of the laser,and hence the frequency of each component of the comb,can be controlled by a microwave frequency standard.

Table6.2. Practical information concerning atomic time and frequency standards.Numerical values indicate orders of magnitude.They correspond to different performance levels or degrees of development.   

<table><tr><td>Type of standard</td><td>Volume (dm3)</td><td>Mass (kg)</td><td>Cost (10³ Euro)</td></tr><tr><td>Laboratory caesium</td><td>500-3000</td><td>500-1000</td><td>1000</td></tr><tr><td>Commercial caesium</td><td>10-30</td><td>10-30</td><td>50-80</td></tr><tr><td>Active hydrogen maser</td><td>150-250</td><td>75-250</td><td>150-450</td></tr><tr><td>Passive hydrogen maser</td><td>20-80</td><td>20-60</td><td>75-150</td></tr><tr><td>Rubidium</td><td>0.2-1</td><td>0.4-1.5</td><td>3-8</td></tr><tr><td>Mercury ion</td><td>10-250</td><td>10-250</td><td>150-2000</td></tr></table>

Table6.3. Typical inaccuracies for various types of atomic frequency standard,as of 2000.   

<table><tr><td>Type of standard Inaccuracy</td></tr><tr><td>Laboratory caesium: cold atom fountain 1 × 10-15</td></tr><tr><td>Laboratorycaesium:</td></tr><tr><td>continuousbeamfromoven 6 × 10-15-10-13</td></tr><tr><td>Commercial caesium 1.5 × 10-12-3 × 10-11</td></tr><tr><td>Hydrogen maser 2-5 × 10-12</td></tr><tr><td>Trapped mercury ion 3.5 × 10-15-2 × 10-13</td></tr><tr><td>Rubidium No meaning (calibration required)</td></tr></table>

# 6.9 Conclusion

In this chapter, we have described the state-of-the-art as far as atomic time and frequency standardsareconcerned.Table6.2 gives somedetailsconcering the volume, mass and cost of such instruments.

Figure 6.11 gives an overview of current frequency instabilities.The other important characteristic is inaccuracy,summarised in Table 6.3.

We have also mentioned some current developments. It may be hoped that, within a short space of time,standards will be produced with frequency insta bilities of $1 0 ^ { - 1 6 }$ for $\tau = 1$ day,and inaccuraciesaprachng $1 0 ^ { - 1 6 }$ .There are possibilities for further improvements,too.Referring toFigure 4.3,which shows schematically how the quality of artificial clocks has evolved,we may thus fully justify an optimistic extrapolation beyond the year 2000.

# 7

Atomic time measurement

The scientific and technical work that serves as a foundation to atomic time measurement has been described in the previous chapters. Chapter 4 showed how such measurements have gradually displaced astronomical measurements. In the present chapter, after recalling the atomic definition of the second and defining the main time scales issuing from it, we shall be concerned with the wayatomic time measurements are put to use. We describe all the steps involved in setting up and disseminating a worldwide time scale that can be used both for synchronisation and as a way of providing a unit of time. We also discuss time scales suitable for dynamical purposes.

# 7.1 Definitions

# 7.1.1 Definition of the second

Letus recall the definition adopted by the 13th General Conference on Weights and Measures (CGPM) in 1967:

The second is the duration of 9192 631 770 periods of the radiation corresponding to the transition between the two hyperfine levels of the ground state of the caesium 133 atom.

As explained in Chapter 3, the second should be considered as the unit of proper time along the worldline of the relevant caesium atom. Since the atoms are moving relative to the device that observes their frequency,i.e., the clock, corrections must be made to allow for this motion in order to ascertain the proper time of the clock. At present levels of accuracy, the only relativistic effect that needs to be taken into account is the second order Doppler effect of special relativity. However, the time may soon come when the whole clock will need to be treated within the framework of generalrelativity,inorder to provide the proper time at a specified point, such as a connector.

If the clock is in the immediate vicinity of,and fixed with respect to the observer,it canbe usedas in classical physics,provided that weaccept Einstein's principle of equivalence. If it is atsome distance,carried byasatellte,for example,and communicates data by radio,then this data must be processed as indicated in Chapter5.

# 7.1.2 International Atomic Time and its relationship with geocentric and barycentric coordinate times

As explained in Chapter 3 (Section 3.3.2e), International Atomic Time (TAI) can be viewed as an average of clock readings. The clocks in question here operate in accordance with the definition of the second. They are assumed fixed relative to the Earth and located on the rotating geoid. These definitions specify the scale unit of TAI, but the whole system of graduations remains to be fitted together somehow. This problem is referred to as fixing an origin. The task was accomplished by assigning the same date in TAI and Universal Time (UT) to a fictitious event, occurring on 1 January 1958 at $_ { \textrm { 0 h } }$ UT. (To be precise,the form UT2of Universal Time was used,as defined in Section8.1.3.) UTis based on the Earth's rotation and is not measured as accurately as TAI. Moreover, it was subsequently recognised that systematic errors were made when determining UT in 1958,and UT values had to be corrected by several milliseconds. However, these corrections were not carried over to TAI. We may therefore say that the origin of TAI is simply fixed by the very existence of this time scale,the coincidence with UT on 1 January 1958 being merely approximate.

In Chapter 3,we defined the geocentric coordinate time. The scale unit for this ideal time is obtained theoretically from the definition of the second.However,an origin must also be fixed in this case.In1991,the International Astronomical Union (IAU) did just this in its Resolution A4,by defininga particular geocentric coordinate time denoted TCG such that

$$
T C G - T A I = 3 2 . 1 8 4 \ \mathrm { s ~ \ o n ~ 1 ~ J a n u a r y ~ 1 9 7 7 , 0 h ~ T A I ~ } .
$$

The number 32.184 appearing here should be treated as exact by convention,as should the date. Note, however,that there is an uncertainty in the TAI rading, something like $1 ~ \mu \mathrm { s }$ at that epoch,so that TCG can be said to float by this amount. In practice, this has little importance.

We also saw in Chapter 3 that a variant geocentric coordinate time was defined having a scale unit with duration very close to the duration of the (proper)

second on the rotating geoid. This variant is Terrestrial Time (TT), related to TCG by the expression for the difference in seconds,

$$
T C G - T T = L _ { \mathrm { G } } \times \cdot 8 6 4 0 0 \times \Delta D ,
$$

where $\Delta D$ is the time elapsed in TAI days since 1 January 1977 at $0 \mathrm { h }$ TAI and $L _ { \mathrm { G } }$ has a conventional valuet

$$
L _ { \mathrm { G } } = 6 . 9 6 9 2 9 0 1 3 4 \times 1 0 ^ { - 1 0 } .
$$

TAI is thus a realisation of TT,up to the 32.184 s offset. We may therefore write

$$
T T ( T A I ) = T A I + 3 2 . 1 8 4 \mathrm { ~ s ~ } ,
$$

adopting the commonly used notation whereby $U ( x )$ represents the realisation of the theoretical quantity $U$ identifiedby the symbol $\mathcal { X }$ . Hence, TT(TAI) should read ‘realisation of TT based upon TAI'.

The reader may wonder why there is a difference of 32.184 s between TT and TAI. In 1958, it was justifiable to fix TAI onto UT rather than Ephemeris Time (ET), because the latter was rather poorly determined. Later, however, astronomers wanted TT to replace ET. All attempts either to shift TAI or to change the argument of the astronomical ephemerides failed. The number 32.184 represents the best estimate of the deviation in seconds between ET and TAI on 1 January 1977.

Let us now consider the barycentric coordinate time mentioned in Section 3.3.2b. This is used to study planetary motions and the trajectories of space probes. The word ‘barycentric’ is intended to mean ‘centred on the centre of mass of the Solar System’. As for TCG,the scale unit is based on the (proper) second. The origin of one particular barycentric coordinate time denoted TCB is such that TCB has the same reading as TCG on 1 January 1977 at $0 \mathrm { h }$ TAI at the centre of mass of the Earth. It is essential to specify at the centre of mass of the Earth’ because the relationship between these two coordinate times is four-dimensional. To order $c ^ { - 2 }$ , it is given by‡

$$
T C B - T C G = \frac { 1 } { c ^ { 2 } } \left\{ \int _ { t _ { 0 } } ^ { t } \left[ \frac { v _ { \mathrm { E } } ^ { 2 } } { 2 } + U _ { \mathrm { P } } ( \mathbf { x } _ { \mathrm { E } } ) \right] \mathrm { d } t + \mathbf { v } _ { \mathrm { E } } . ( \mathbf { x } - \mathbf { x } _ { \mathrm { E } } ) \right\} \ ,
$$

where $\mathbf { X } _ { \mathrm { E } }$ and $\mathbf { v } _ { \mathrm { E } }$ denote here the barycentric position and velocity of the centre of mass of the Earth, whilst $\mathbf { x }$ is the barycentric position of the observer and

$U _ { \mathrm { P } }$ the Newtonian gravitational potential due to all the bodies in the Solar System except for the Earth itself. In the integral, $t = T C B$ and $t _ { 0 }$ is chosen in accordance with the origins indicated previously.On the Earth’s surface,the last term reaches a maximum value of $2 . 1 ~ \mu \mathrm { s }$

For terrestrialobservers,the integral in (7.5) gives rise to an increment proportional to the time,rising at a rate of about $0 . 5 \mathrm { ~ s ~ }$ per year, to which periodic terms must be added. The largest of the latter is due to the fact that the Earth's orbit is elliptical. It is thus annual, with half amplitude equal to $1 . 7 ~ \mathrm { m s }$ To reach an accuracy of $1 0 0 ~ \mathrm { { n s } }$ ,more than one hundred periodic terms must be taken into account [7.1].

Towards 197o, it became necessary to use a relativistic model to calculate the ephemerides of bodies in the Solar System. In 1976, the IAU defined the temporal argument of the ephemerides by carrying out a scale unit transformation on the barycentric coordinate time in such a way as to leave only the periodic terms in the difference with TT. In 1979,the new time scale was given the name TDB (Temps dynamique barycentrique). At this time, some astronomers had raised doubts about general relativity,so that all reference to this theory and its terminology was scrupulously avoided. The relation between TDB and TCB,inseconds,is given by

$$
T C B - T D B = L _ { \mathrm { B } } \times 8 6 4 0 0 \times \Delta D ,
$$

where $\Delta D$ has the same meaning as in (7.2) and $L _ { \mathrm { B } }$ is currently estimated to be

$$
L _ { \mathrm { B } } = 1 . 5 5 0 5 1 9 7 6 8 \times 1 0 ^ { - 8 } \pm 2 \times 1 0 ^ { - 1 7 } \ .
$$

Like TT,which was given the name TDT(Temps dynamique terrestre) between 1979 and 1991, both TCB and TDB can be represented on the basis of TAI, with the help of relations (7.2), (7.5) and (7.6). The use of TDB instead of TCB gives rise to theoretical complications. However,a great deal of work has been carried out taking TDB as time argument, particularly the construction of the Jet Propulsion Laboratory ephemerides,which are used for planetary exploration. For this reason, it is difficult to make the desired transition to TCB.

Figure 7.1 sums up the relationships between the various coordinate time scales.

![](images/1fe9ded63953575792db8804ecb127c3f77d6977e7521ef725c6237330cafcbd.jpg)  
Fig. 7.1. Relationships between coordinate time scales starting from the proper time $\tau$ of an observer. Barycentric and geocentric channels are related by four-dimensional transformations,sothatTAIcan beused torealisealltheoretical times.Quantities $L _ { \mathrm { B } }$ ， $L _ { \mathrm { G } }$ and $\Delta D$ are defined in the text.

# 7.2 Establishing International Atomic Time

# 7.2.1 Time scale algorithms

When several atomic clocks are available, their readings can be used to set up a single time scale. This is certainly more reliable than time scales based on the contributing clocks taken separateiy, and hopefully, has better characteristics than any of them.

If the clocks are sufciently local,in thesense that theyare not too widely separated, they can be used to establish the proper time of their laboratory without it being necessary to take into account any other relativistic effects than the second order Doppler effect from special relativity. If the clocks are spread across a country or around the world.a realisation of TT is usually constructed.

This is what happens,for example, when TAI is established. In this case, the proper time $\tau _ { \mathrm { C } }$ of each clock Cmustbetransformed intoanapproximation $\underline { { t } } _ { C }$ of TT,before the datacan becombinedaswould have beendone toestablish a local time scale.This transformation introduces an arbitrary additive constant, but we shallsee that it presents no obstacle. In order to simplify notation, tc will be written $t _ { \mathrm { C } }$ throughout the present chapter.

Before setting up an algorithm for some time scale that we intend to construct,at least the following set of questions should be asked:

· Over what sampling period do we wish to optimise frequency stability?   
· Do we wish to impose a certain frequency accuracy,and if so,what would be an acceptable compromise in the case where this affects stability?   
What should be the interval between clock comparison dates (the data acquisition period)?   
How long is the interval between the date at which the calculated scale becomes available and the last date for which this scale has been calculated?   
· How often is the calculation to be updated?

The various time lapses involved are shown in Figure 7.2.

Answers to these questions are interdependent. For example, if we seek long term frequency stability, we can accept a longer interval between clock comparisons than when short term stability is required. A wide range of situations nevertheless remains open. In some applications,the scale must be obtained almost in real time,whilst for TAI,a two month delivery time isacceptable. For the study of pulsars,where the highest possible quality is sought, nobody would complain about waiting a whole year. It is not therefore possible to describe a typical algorithm. Besides,algorithms must yield to technical constraints,such as the invention of new clocks or new methods of time comparison.All algorithms nevertheless exhibit certain common features,although they may be hidden to some extent by the mathematical formalism. These can be exposed by examining the algorithmset up by the BIH in 1973 and still used by the BIPM to establish TAI, apart from a few adaptations to accommodate technical advances [7.2,7.3].

# 7.2.2 Algorithm for International Atomic Time

(a) General organisation

International Atomic Time is currently based upon data from over 2o0 atomic clocks and frequency standards in about sixty different laboratories and compared via the Global Positioning System, its Russian counterpart GLONASS, and the Two-Way Satelite Time and Frequency Transfer (TWSTFT) method (see Section 5.6.3).

![](images/9aa28ab9761c018fd1f8b561396016af1b2faed6b9971f346aeafe0ccfd90628.jpg)  
Fig.7.2. Schedule for carrying out time scale algorithms. Data comprises either clock time differences,or other information that can be used to calculate such differences (e.g., reception dates of GPS signals).

It is set up in such a way as to favour long term frequency stability,over periods of a month or more,and frequency accuracy. Because of the long term stability, it becomes acceptable to allow a rather long time for publication of TAI, between one and two months. Indeed, time differences between local clocks and TAI can be extrapolated to yield an approximation of TAI in real time.

TAI is established in two stages. A stability algorithm produces what is known as the Echelle atomique libre (EAL),a free-running mean time scale whose stability is optimal for the relevant sampling period. Then a long term servo control based on the frequency of primary standards constructs TAl by applying a time dependent correction $[ T A I - E A L ] ( T A I )$ to the EAL. This so-called steering aims to ensure the frequency accuracy of TAI.

The schedule is as follows (see Figure 7.2).

· Computation period: one month. The date $t _ { 0 }$ is around the middle of month   
$m$   
Data acquisition rate: every five days (at $0 \textrm { h }$ UTC on dates ending in 4   
or 9 when expressed in Modified Julian Date (MJD)). Data was previously acquired every 10 days, up to the end of 1995.   
Last date covered by the publication: $t _ { 3 }$ somewhere around the end of month   
$m - 1$   
There is almost no further data (i.e., $t _ { 2 } - t _ { 3 } = 0$ ).   
Transmission takes a few days (including preparation of data in participating laboratories).This involves a certain level of commitment on the part of the various laboratories and the BIPM.

# (b) Stability algorithm

We begin by considering an imaginary situation in which all participating clocks $I$ ${ \boldsymbol { I } } = { \boldsymbol { \mathrm { J } } }$ ，K,etc.)are read simultaneously,according totheconvention of coordinate simultaneity,at the date $t$ in geocentric coordinate time (TCG, TT or TAI). The readings $\tau _ { I } \left( t \right)$ are transformed into $t _ { I } \left( t \right)$ ,introducing arbitrary integration constants.Letting $\{ \} ( t )$ denote a weighted mean over the clock ensemble at the date $t$ ,EAL could be defined by

$$
\left[ E A L \right] ( t ) = \left\{ t _ { I } \right\} ( t ) ,
$$

assigning statistical weights in accordance with the chosen stability criteria.

Definition (7.8) can serve the required purpose as long as allthe clocks continue to operate, weights are not modified,and new clocks are not introduced. This is summarised by saying that the clock ensemble must remain invariable. If the ensemble is altered in some way, it is clear that this will cause a time step to occur, since the clocks do not all have the same reading,and it will also cause a frequency jump, since the clocks do not all have the same frequency. In order to avoid this situation, definition (7.8) is replaced by

$$
\left[ E A L \right] ( t ) = \{ t _ { I } \} ( t ) + A + B ( t - t _ { 0 } ) ,
$$

where $t _ { \mathrm { 0 } }$ is some arbitrarily chosen origin. $A$ and $B$ are constants which are modified when the clock ensemble is altered, in such a way as to maintain time and frequency continuity. Let $t _ { \mathrm { m } }$ be the date at which some modification is made. Let us denote the old values of $A$ and $B$ by $A _ { - }$ and $B _ { - }$ ,and the new values by $A _ { + }$ and $B _ { + }$ . The requirement of time continuity is expressed by

$$
A _ { + } = A _ { - } + \{ t _ { I } \} _ { - } ( t _ { \mathrm { m } } ) - \{ t _ { I } \} _ { + } ( t _ { \mathrm { m } } ) - ( B _ { + } - B _ { - } ) ( t _ { \mathrm { m } } - t _ { 0 } ) ~ ,
$$

the ensemble averages $\{ t _ { I } \} _ { - } ~ ( t _ { \mathrm { m } } )$ and $\{ t _ { l } \} _ { + } \left( t _ { \mathrm { m } } \right)$ being calculated at $t _ { \mathrm { m } }$ for the old and new ensembles,respectively. Consider the case where one clock has stopped running. Then tm is the last date for which that clock still gave data. It is therefore included in $\left\{ t _ { I } \right\} _ { - }$ ( $t _ { \mathrm { m } }$ )but not in $\{ t _ { I } \} _ { + } ( t _ { \mathrm { m } } )$ As far as continuity of frequency is concerned,this imposes

$$
B _ { + } = B _ { - } + \left\{ { \frac { \mathrm { d } t _ { I } } { \mathrm { d } t } } \right\} _ { - } - \left\{ { \frac { \mathrm { d } t _ { I } } { \mathrm { d } t } } \right\} _ { + } ,
$$

where derivatives are calculated at $t _ { \mathrm { m } }$

Whereas it is a straightforward and rigorous matter to calculate $A _ { + }$ once $B _ { + }$ has been found, it is actually impossible to obtain $B _ { + }$ from (7.11) for the simple reason that we cannot evaluate instantaneous frequencies. (We can change origin, choosing $t _ { 0 } ~ = ~ t _ { \mathrm { m } }$ .The $B \mathrm { s }$ are then not needed to calculate $A _ { + }$ .)We must work with mean frequency values. Before $t _ { \mathrm { m } }$ ,a duration must be chosen over which to calculate these mean frequencies. After $t _ { \mathrm { m } }$ , no data is available if we wish to produce the time scale in real or near real time. Consequently, we must predict the frequency of each clock on the basis of its past behaviour.

Asubtle problem arises when we consider (7.11), because the derivatives are with respect to the unknown ideal time $t$ .However,only a difference between two such derivatives is required. This means that t can be replaced by a physically realised time scale, provided that its frequency is stable enough and lies close enough to that of $t$ . In practice, the EAL itself can fulfill this purpose. Hence, using past frequency differences with respect to the EAL for each clock,we atempt to predict future values of this diference.

Frequency prediction and weighting form the core part of time scale algorithms. Another importanttask must beadded,namely,thedetection of anomalous behaviour in one of the clocks,which leads to its being withdrawn from the ensemble. Such statistical problems are challenging. The type of solution brought to bear can significantly influence the quality of the scale that is finally produced.

We now transform the above equations so that they can be applied to real measurements. These measurements are proper time differences between clocks,obtained by the methods described in Chapter 5.Let us recal that these are differences in readings at the same date $t$ , but that, since they vary only slightly with time,they can be dated by areference scale 0,for which there remains a great freedom in the choice. In practice, Coordinated Universal Time (UTC) is used. Starting with the proper time differences for two clocks J and

K. we calculate the differences in the coordinate times $t _ { \mathrm { J } }$ and $t _ { \mathrm { K } }$ , fixing the constants of integration in anarbitrary manner.This gives

$$
\left[ t \mathrm { J } - t _ { \mathrm { K } } \right] ( \theta ) = \delta _ { \mathrm { J K } } ( \theta ) ~ ,
$$

where $\delta _ { \mathrm { J K } }$ is the measured value. Putting

$$
x _ { I } ( \theta ) = \left[ E A L - t _ { I } \right] ( \theta ) ~ ,
$$

equations (7.9) and (7.12) become

$$
\left\{ x _ { I } \right\} ( \theta ) = A + B ( \theta - \theta _ { 0 } ) ,
$$

$$
x _ { \mathrm { J } } ( \theta ) - x _ { \mathrm { K } } ( \theta ) = - \delta _ { \mathrm { J K } } ( \theta ) ~ ,
$$

where the factor $t - t _ { 0 }$ is replaced by $\theta - \theta _ { 0 }$ ,since $B$ is extremely small (of the order of $1 0 ^ { - 1 3 }$ ).The time comparison network is organised insuch a way that the system formed by (7.14) and equations of type (7.15),writen for various pairs of clocks,can be solved exactly,because the processing of superfluous links brings with it more drawbacks than advantages.When the clock ensemble changes, $A$ and $B$ are reestablished using

$$
A _ { + } = A _ { - } - \left\{ x _ { I } \right\} _ { - } ( \theta _ { \mathrm { m } } ) + \left\{ x _ { I } \right\} _ { + } ( \theta _ { \mathrm { m } } ) - ( B _ { + } - B _ { - } ) ( \theta _ { \mathrm { m } } - \theta _ { 0 } )
$$

and

$$
B _ { + } = B _ { - } - \left\{ { \frac { \mathrm { d } x _ { I } } { \mathrm { d } t } } \right\} _ { - } + \left\{ { \frac { \mathrm { d } x _ { I } } { \mathrm { d } t } } \right\} _ { + } ,
$$

where,as before, $t$ is replaced by EAL in derivatives.

Having obtained the solution for $x _ { I }$ , it is transformed to $\mathrm { E A L } - \tau _ { I }$ using the theoretical relation between $\tau _ { I }$ and $t _ { I }$ ,with the same value for the constant of integration as for the inverse transformation. EAL is then available at the location of the participating clocks through a correction to their readings.

When calculations are made, we use the fact that all clocks currently participating in the construction of the EAL are fixed on the Earth. The transition from their proper time to coordinate time only involves a fixed frequency shift. This shift is not applied explicitly. It is contained in the correction term $B$ . It follows that the stability algorithm provides $\mathrm { E A L } - \tau _ { I }$ directly. However,if we wanted to incorporate satellite-borne clocks,a full treatment would be needed. The previously noted simplification whereby $\theta _ { 0 }$ is made to coincide with $\theta _ { \mathrm { { m } } }$ ， leads to a change in $\theta _ { 0 }$ each time the ensemble is modified.

# (c) Frequency steering

A stability algorithm like the one just described optimises stability over a sampling period that has been fixed by choosing the way frequencies are predicted. In its application to the EAL, we shall see that this optimal value is somewhere between 3O and 6O days. However, the algorithm contains no guarantee against longer term fluctuations. Step by step adjustment of the $B s$ may even lead to an unbounded frequency drift.

The first problem to solve is how to evaluate the frequency of the EAL, using data from primary standards. In this discussion,all frequencies are referred to the level of the rotating geoid.

A primary standard provides an estimate of the mean frequency of the EAL between dates $\theta _ { \mathrm { i } }$ and $\theta _ { \mathrm { f } }$ . As time goes by, whilst this calibration becomes part of the past, the EAL retains a recollection of it, thanks to its frequency stability. Nevertheless, this recollection is not perfect and a contribution from the frequency instability of the EAL must be added to intrinsic uncertainties in the standard.

A filter has been devised which yields an optimal value for the mean frequency of the EAL over a given interval by assigning coefficients (with sum 1) to all available calibrations,whether they come before or after. The word ‘filter’ is used,rather than weighting, because some of the coefficients may be negative. This filter takes into account the following factors:

· a statistical model for frequency noise in the EAL, sum of a white phase noise (arising from time comparisons),and white, flicker and random walk frequency noise (due to the clocks); · random and systematic uncertainties in frequency calibrations; · initial and final dates of each calibration and of the period of estimation.

The theory behind this is rather complex and willnot be discussed here. An account can be found in [7.4].

Steering consists in finding a function $P \left( \theta \right)$ allowing us to deduce TAI from the EAL by

$$
T A I ( \theta ) = E A L ( \theta ) + P ( \theta ) ,
$$

in such a way that the TAIfrequency remains close to the results of the accuracy filter, without its stability being degraded with respect to that of the EAL. For example, if the TAI frequency were immediately changed each time a new calibration occurred, frequency jumps would be unacceptable. To avoid this situation, the frequency instability of $P \left( \theta \right)$ is arranged to be smaller than the estimated frequency instability of the EAL.

# (d) Application

The following is a highly schematic description,since steady advances arebeing made in the design of atomic clocks and time comparisons,and the BIPM algorithms must have acertain level of flexibility in order to adapt. Our discussion refers to the situation at the end of 20oo. However,the initial assessment of the role to be played by TAI,as carried out by the BIH in 1973,has been regularly confirmed by international organisations. For this reason,the basic principles have not changed since then.

When calculations are carried out, whole seconds are omitted. They are fed back in whentheresultsareobtained.We maythus consider thatthefollowing explanations apply equally to either TAI or UTC.

Time comparison network. Let $k$ denote a laboratory contributing to TAI. Each laboratory $k$ has a master clock which supplies an approximation $\mathrm { U T C } ( k )$ to Coordinated Universal Time UTC. This clock serves as a reference for all local dating procedures.In particular, it measures the time differences $U T C ( k ) - \tau _ { \mathrm { C } }$ for all clocks C of laboratory $k$ . The BIPM only uses values measured every five days on standard dates.Theseare defined to be Modified Julian Dates (MJD) ending with a 4 or a 9,at $0 \mathrm { h }$ UTC.

Remote time comparisons concern the $\mathrm { U T C } ( k )$ .Although continuous, the BIPM estimates them on standard dates by averaging or filtering.Figure 7.3 shows the network of time transfer links.A few laboratories act as centres for links up to about $1 0 0 0 \mathrm { k m }$ ,using GPS or GLONASS. These centres are linked together bythe best available techniques,namely,TWSTFTand GPS,usingfor the latter precise ephemerides,computed retrospectively,and measured values for ionospheric corrections. In certain countries, there is a further level in the hierarchy,whereby acentral laboratory provides the link with several national laboratories. This has long been the case in France,for example.

Stability algorithm. The stability algorithm,called Algos,calculates the values of $E A L - U T C ( k )$ at the standard dates in one month batches. The initial and final dates of these batches are the last standard date in the month. (The duration of one batch is normally 30 days,but it is sometimes 35 or 25 days.) Quite arbitrarily,these beginning and end datesof the batches have been chosenas ensemble modification dates,i.e.,the previously defined $\theta _ { \mathrm { { m } } }$ .Consequently,clock weights are held constant over each monthly interval.A clock weight is zero when a clock has provided incomplete data, either because it has stopped or because it has entered the ensemble after the beginning of the interval.

![](images/d222bb577268242e7338e1d6c4210c2c89dfe62557477373be25faba6685e808.jpg)

At the present time (20oo), Algos processes the data from more than 200 clocks,mainlycommercially manufactured caesium clocks whichave excellent long term stability. Since only stability is relevant here, other types of clock can contribute.There are about forty hydrogen masers and their number now remains stable.

The ensemble average is a weighted mean. The weight of a clock C is proportional to the reciprocalof the variance $\sigma _ { \mathrm { C } } ^ { 2 } ( 1 2 , \tau )$ of 12 mean frequency samples taken over one month,relative to the EAL $^ \dagger$ This variance has been chosen,rather thantheusual two-samplevarnce $\sigma _ { y , \mathrm { C } } ^ { 2 } ( \tau )$ , in order to reduce the weight of clocks exhibiting frequency drift,or annual frequency fluctuations,as has sometimes been observed. In the flicker noise frequency model, which is suited to the values of $\tau$ considered,

$$
\sigma _ { \mathrm { C } } ^ { 2 } ( 1 2 , \tau ) = 2 \sigma _ { y , \mathrm { C } } ^ { 2 } ( \tau ) .
$$

As frequency fluctuations of clocks are evaluated with respect to the EAL to which they contribute, some clocks may progressively gain an excessive statistical weight and unduly dominate the ensemble.The problem is avoided by using an upper limit for weighting. This has been modified several times, in order to cope with clock improvements. Since January 1998,the rule is that no clock can receive a weight exceeding $0 . 7 \%$ of the total weight. However, with the increasing role played by the latest commercial caesium clocks,this rule is becoming unsatisfactory because it does not suficiently discriminate between these clocks.A relative upper limit $L$ in the form $L / N$ is currently under study (November 2000),where $N$ is the total number of clocks and $L$ lies between 2 and 3.

In order to detect anomalous behaviour in a clock, a comparison is made between its mean frequency with respect to the EAL over the last month, that is,over the month for which the TAI is currently being calculated,and its mean frequency with respect to the EAL over the preceding 11 months. If the variation is more than three times what might be expected from random fluctuations,the weight of the clock is set to zero. All clocks undergo this test. The calculation is repeated once offending clocks have been eliminated. Four iterations are applied.

Frequencies are predicted by simple continuation of the observed frequency, always relative to the EAL, over the preceding month. Many studies of real data have failed to yield a better prediction for the aim in question.

Any new clock remains under observation for at least four months before effectively taking part in TAI. Over this period, it enters the calculations, but with zero weight. When the number of frequency samples $n$ is less than 12. $\sigma _ { \mathrm { C } } ^ { 2 } ( 1 2 , \tau )$ is estimated from $\sigma _ { \mathrm { C } } ^ { 2 } ( n , \tau )$ ,assuming a flicker noise frequency model.

With the Algos algorithm,it is possible to apply different weighting and prediction rules according to the type of clock. For example, it would be feasible to take into account a frequency drift in the hydrogen masers. Up to now, this option has not been implemented.

As an example, consider the laboratories and clocks taking part over the period 28 August 2000 to 27 September 2000. The BIPM received data from 221 clocks(179 caesium clocks and 42 hydrogen masers) spread over 39 laboratories or national institutes, the latter incorporating several laboratories each. 121 clocks were assigned the maximal weight, including 98 of the latest commercial caesium clocks, 4 primary caesium clocks (built in research centres), and 17 hydrogen masers. Zero weights were attributed to 44 clocks,mainly new ones in their probationary period. Finally, 56 other clocks received intermediate weights, generally rather low.

Clocks assigned the maximal weight constitute $8 5 \%$ of the total, and this proportion is too high,as noted above.

Frequency steering. In 1969, using the Loran-C navigation system, the BIH was able to drop the mean frequency approach to calculating TAI (then known as TA(BIH)), replacing it by one averaging over time. However, it did not have access to data from individual clocks.TAI was an average of atomic time scales set up by a small number of large national timing centres. It was calculated by means of an algorithm similar to Algos [7.5]. Originally, the correction $B$ in the defining equation of type (7.9) was zero for the three participating timing centres, viz.,the United States Naval Observatory (USNO),the Physikalisch-Technische Bundesanstalt (PTB) in Germany,and the Commission nationale de l'heure (F) at the Paris Observatory. No attempt was made to connect frequencies with previous values of TAI, nor to align with data from primary standards, since such data was too sparse and too uncertain.

In I973,having organised direct access to individual clock data, the BIH implemented the Algos algorithm. Care was taken to avoid any frequency jump by suitably adjusting the initial value of $B$ . TAI was produced directly by Algos,in other words, it was just equal to the EAL. However, primary standards had seen much progress and showed right from the start that the TAI frequency was too high by about 10 × 10-13.

This frequency error was corrected on 1 January 1977 bya jump of exactly 10 × 10-13 in the TAI frequency, following a resolution adopted by the IAU in 1976.

![](images/b7a5d4e5b4e7fa2420a1e43e121689b56d0b7af833a507a4d0b13b10127e015b.jpg)  
Fig. 7.4. Duration $( 1 + d )$ s of the TAI scale unit on the rotating geoid (bimonthly values).

Having done this, it became possible to introduce frequency steering,as had already been envisaged in 1974 by the Consultative Committee for the Definition of the Second (CCDS). Application had been postponed because the frequency error to be compensated was too great. At the beginning, the function $P ( \theta )$ was a succession of linear functions, with frequency jumps of $2 \times 1 0 ^ { - 1 4 }$ occurring,when needed,at intervals of more than two months. The size of the discontinuities was reduced in several stages to reach $1 0 ^ { - 1 5 }$ in 1996, and these jumps may be made at monthly intervals.Figure 7.4 shows the bimonthly mean values of the duration of the TAI scale unit in seconds on the rotating geoid. The offset of about $2 \times 1 0 ^ { - 1 4 }$ prior to1996 results from the omission of acorrection for blackbody radiation (see Section 6.4.1e). The decision to apply this correction toall primary standards was taken in March 1996.The frequency offset has been gradually reduced by steering.

Whereas Algos optimises stability over one or two months, steering guarantees stability over much longer periods. It can be considered as a way of introducing a new weighting. As the sampling period increases,each clock contributing to the EAL affects TAI less and less,whilst primary standards have more and more relative importance. For stability over about 5 years,all the weighting is carried by primary standards.

Form of results. After steering corrections,TAI is known from the values of $T A I - U T C ( k )$ at standard dates. In fact, the BIPM publishes the values of

$U T C - U T C ( k )$ every month in its Circular T, available by electronic mail. An example is shown in Figure 7.5. Apart from this, by tracking GPS and GLONAsS satellites for time comparisons, values of $U T C - G P S$ Time and $U T C - G L O N A S S$ Time are provided with similar uncertainties to those in $U T C - U T C ( k )$ Timing centres $k$ ,and GPS and GLONASS satellites form the network of primary access points to TAI and UTC.

It is important to note that TAI and UTC become definitive once published. Small corrections have sometimes been allowed (amounting to a few nanoseconds),but never any global revisions. Even these small corrections are now avoided. It follows that, if errors, from whatever source,are not detected during calculations, they are incorporated forever into TAI. The recognition and elimination of these errors are a key task for Algos and preprocessing programmes,to which onlya few days can be devoted.

# 7.3 Properties of TAI and UTC

# 7.3.1 Reliability

Reliability is guaranteed by the international basis of TAI. Imagine for a moment what would happen if, just as a practical joke, someone found a way to stop all atomic clocks, just for a short time. This would cause such a tremendous disturbance in world affairs that the loss of TAI would be a totally insignificant matter!Furthermore, when it came to setting it up again, the phase of TAI could be retrieved to within a few tenths of a microsecond by observations of rapidly rotating pulsars (see Chapter 8).

# 7.3.2 Accuracy of readings

The uncertainty in TAI readings using values of $U T C - U T C ( k )$ in one of the primary access laboratories $k$ is approximately equal to the uncertainty introduced by this laboratory in time comparisons used to form TAI. It represents the smallest possible uncertainty when dating an event with TAI in the laboratory under consideration. In the best equipped laboratories, this uncertainty is estimated (in 2ooo)atabout ten nanoseconds,taking uncertainties in instrumental delays into account.

Access afforded to TAI by receiving GPS signals and using values of $U T C \mathrm { ~ - ~ } G P S$ Time introduces uncertainties of the same order, in a laboratorypossessng thebestavailableequipmentbyaveraging overagreatmany trackings for at least one day. The same can be said for GLONASS.

![](images/0a14ceefd56ec5c4bd66ddbc4a2359c84aa991063f6e7269b1b1a860dee3156d.jpg)  
Fig.7.5. First page of BIPM Circular T.

# 7.3.3 Frequency stability

Ordinate values in Figure 7.4 represent,after sign change, differences in normalised frequencies between TAI and'the set of primary standards (on the geoid). An annual fluctuation is observed. Its total amplitude was close to $1 0 ^ { - 1 3 }$ over the period 1977-1982 but then gradually fel to around $1 0 ^ { - 1 4 }$ in 1993-1995, before virtually disappearing altogether. Is this due to TAI or to the primary standards? When the amplitude was large, it seems that fluctuations were mainly due to environmental influences on commercial caesium clocks, with humidity being the dominating factor. This weak point was gradually rectified, either by improving clocks,or by giving them better protection. The tiny magnitude of the fluctuation remaining in 1995 may still be caused by environmental influences acting while time comparisons are made. The temperature sensitivity of certain GPS receivers has already been mentioned. There may also be inadequacies in the way refraction has been modelled,in particular,tropospheric refraction, which is never measured. Primary standards appear to be exempt from detectable annual variations.

The stability of TAI can be estimated by comparison with other atomic time scales maintained by several timing centres. Instabilities shown in Figure 7.6 were calculated for sampling periods $\tau$ ranging between 10 and 160 days. In fact, these are instabilities in the EAL in 1999 and 200O [7.6], but for these values of $\tau$ , they differ only slightly from the instabilities in TAI. For longer $\tau$ ， instability is estimated under the assumption that current properties of clocks and primary standards remain the same indefinitely. It levels out at around $5 \times 1 0 ^ { - 1 5 }$ as aresult of frequency stering.Frequency accuracy imposes an upper limit on very long term instability.

# 7.3.4 Frequency accuracy

Let $d _ { \mathrm { T A I } }$ be the relative deviation of the TAI scale unit from the TT scale unit (the SI second on the rotating geoid),i.e.,the relative frequency deviation of TAI with the opposite sign $d _ { \mathrm { T A I } } = - y _ { \mathrm { T A I } } )$ . The monthly average of $d _ { \mathrm { T A I } }$ is normally less than $\pm 1 0 ^ { - 1 4 }$ . Its value is supplied retrospectively by the BIPM, together with its standard uncertainty $u$ .The latter is estimated with great care, taking into account uncertainties in the primary frequency standards and in their links with TAI. At the end of 200O, the value of $u$ lay in the range $2 -$ 3 × 10-15. For example, for the interval 28 August 2000 to 27 September 2000, $d _ { \mathrm { T A I } } = 7 . 3 \times 1 0 ^ { - 1 5 }$ and $u = 2 . 2 \times 1 0 ^ { - 1 5 }$

![](images/82d714e56528ea8dffcc4d69e8d02cb6fc73d7f2de242495bdf1addabd1b8f88.jpg)  
Fig.7.6. Frequency instability of TAI (see text for explanation).

# 7.4 World organisation of time measurement

A worldwide organisation of time measurement gradually came into being as progress was made with atomic clocks and standards,together with improved means for comparing instruments and time scales. Once this organisation had reached a certain maturity, it was recognised and stabilised by the relevant international organisations. Chapter 4 gives an overview of the evolutionary phase. In this chapter,we shall describe the present state of the organisation, which would appear to represent the future at least for the next few years,or even a decade or more.

# 7.4.1 Coordinated Universal Time

As explained in Section 4.5, Coordinated Universal Time (UTC) in its present form is none other than International Atomic Time corrected by a whole number of seconds in order to follow approximately the Universal Time UT1 tied to the Earth's rotation.

Since 1 January 1972, UTC has been run according to the guidelines in Recommendation ITU-R TF 460-4 of the International Telecommunications Union (ITU). This recommendation took root in Recommendation 460 adopted in 1970 by the International Radio Consultative Committee (CCIR),an ITU committee that has since been dissolved. Let us now outline several of the directives and explain how they are put into practice.

# (a) Leap seconds

Jumps of one whole second, referred to by the ITU as ‘the introduction of one positive or negative leap second’,must be introduced at the end of a UTC month,preferably at the end of December or June,otherwise at the end of March or September. It is stipulated that a positive leap second should begin at $2 3 \mathrm { ~ h ~ } 5 9 \mathrm { ~ m ~ } 6 0 \mathrm { ~ s ~ }$ and end at $0 \mathrm { ~ h ~ } 0 \mathrm { ~ m ~ } 0$ s the following day. There is then no ambiguity when events are dated in this way. However,an ambiguity appears in other systems, for example, when fractional days are used. If a positive leap second has been introduced, the date $N . 0 0 0 0 0 5 7 9$ could mean either day $( N - 1 )$ at $2 3 \mathrm { ~ h ~ } 5 9 \mathrm { ~ m ~ } 6 0 . 5 \mathrm { ~ s ~ }$ ,orday $N$ at $\begin{array} { r l } { ~ } & { { } 0 \mathrm { ~ h ~ } 0 \mathrm { ~ m ~ } 0 . 5 \mathrm { ~ s ~ } } \end{array}$ This ambiguity does not arise in the case of a negative leap second. However, the probability that negative leap seconds will be needed is almost zero.

Dates for leap seconds are fixed by the International Earth Rotation Service (IERS) and announced at least 8 weeks beforehand.

The UTC system works well. On 1 January 1972, $T A I - U T C$ was equal to $1 0 ~ \mathrm { s }$ Positive leap seconds have always been introduced at the end of December or the end of June, at a rate of between one per year and one every 2.5 years. From 1 January 1999 up until a date that cannot yet be specified, $T A I - U T C = 3 2 ~ \mathrm { s } .$ The relation between TAI and UTC can be found in the Annual Reports of the IERS and the Time Section of the BIPM.

# (b) Time signals. Code for Universal Time UT1

Time signal emissions conform as closely as possible to UTC. An ITU recommendation fixes a tolerance of $1 ~ \mathrm { m s }$ In reality,the discrepancy is much smaller than this. It is also recommended that the carrier frequency be tuned to the TAI frequencyi $1 0 ^ { - 1 0 }$ ,and that the relationship between time signals and the phase of the carrier wave should be known (e.g.,if the carrier has frequency $1 0 \ \mathrm { M H z }$ , the second pulse should occur every $1 0 ^ { 7 }$ periods).

It is recommended that time signals should carry audible coded information about the difference $U T I - U T C$ .This information is a quantity $D U T I$ ,in the form of an integral multiple of $0 . 1 \mathrm { ~ s ~ }$ , whose value is provided by marking a certain number of second pulses, either by broadening,spliting or any other method. Figure 7.7 shows how the code works. Values of $D U T I$ and their application date are provided one month beforehand by the IERS and they are the same for all emissions.

![](images/d0f8fd7ea79ee834860434a6a2be5ee99ec64b084fc1ae477dd807f5fd79ab9f.jpg)  
Fig. 7.7. Code for $D U T I = U T I - U T C$ transmitted with time signals.Second pulses are emphasised by broadening,splitingor someother audible means.For egative values of $D U T I$ ,the relevant number of pulses ismarked from second 9.

Some time signals also carry coded information $d U T I$ giving the value of $U T I - U T C$ to the nearest $0 . 0 2 \ : s$ , but this isunoficial.Even thecoded information $D U T I$ is rarely used and some emissions no longer include it.

The Annual Report of the BIPM Time Section provides a list of international time signals with their main characteristics.

# (c) Using UTC

Coordinated Universal Time is used as a practical reference worldwide. Its use,like the acronym UTC which is the same in every language,is recommended by international organisations,including the 1971General Conference on Weights and Measures (CGPM) and the ITU.

In different countries around the world, local time is attached to UTC corrected by a whole number of hours. This is sometimes stipulated by written law,as in France (by decree, on 9 August 1978).Legal institutions sometimes prefer to use the national approximation to UTC,as happens in Germany. There are countries in which UTC is not legally recognised,although it is actually used, since no other time scale is readily available.

Let us just recall that the still widespread use of the acronym GMT is not correct when it is intended to refer to UTC,as is the case when expressing the time in general usage.This practice has often been criticised,especially by the IAU. Strictly speaking, it should be replaced by UTC. However,for everyday usage,where inaccuracies of more than one second are of no real import,UT is an acceptable appellation.

As mentioned in Section 7.2.2, the approximation $\mathrm { U T C } ( k )$ to UTC is maintained at a timing centre k. This is usually realised by an atomic clock with an attached device which adds a linear time correction,whilst allowing adjustment of its two parameters. In other cases, this physical device is replaced by calculation, allowing in principle a more complex correction,with a quadratic term,for example. In both cases,every effort is generally made to keep $\mathrm { U T C } ( k )$ as close to UTC as possible. In 1993, the Consultative Committee for the Definition of the Second recommended that timekeeping laboratories supply the information required to facilitate synchronisation with UTC in real time,to within 10O ns,if feasible. One way of achieving this is to ensure $| U T C - U T C ( k ) | < 1 0 0$ ns.

The BIPM's monthly cycle for producing and disseminating $U T C \mathrm { ~ - ~ }$ $U T C ( k )$ requires one to two month extrapolations in order to servo control the $\mathrm { U T C } ( k )$ on UTC. To this end, laboratory $k$ can base its calculations on extrapolations from those of its clocks with the best stability over a sampling period of around one month. However, if this laboratory has several atomic clocks, it is better to construct,on this local level,a time scale known as independent local atomic time. Such a time scale, denoted $\mathrm { T A } ( k )$ ,can be set up much more quickly than TAI/UTC, because local time comparisons are extremely accurate.This then provides a more solid foundation for extrapolating $\mathrm { U T C } ( k )$

In 2000, about fteen laboratories were producing a $\mathrm { T A } ( k )$ by various means.Let us consider some examples. At the US Naval Observatory, the scale TA(USNO) is based on several tens of commercially manufactured caesium clocks and also on hydrogen masers. In Germany, TA(PTB) is directly produced by one of the PTB’s primary standards. In France, TA(F) is calculated by the Laboratoire primaire du temps et des frequences at the Paris Observatory, using data from about twenty commercial caesium clocks spread across the country. The BIPM publishes the values of $T A I - T A ( k )$ in the same way as the values of $U T C - U T C ( k )$ in its Circular T.

The $\operatorname { T A } ( k )$ are not independent of TAI (or UTC) since the same clocks participate in both undertakings. But they are independent of one another and this makes it possible to deduce their instability from the mutual instability of each pair of time scales (using the so-called three-corner hat method mentioned in Section 5.2.8,or indeed the $n$ -corner hat method).

In 1995,only two laboratories in the United States were maintaining their $\mathrm { U T C } ( k )$ to within $1 0 0 ~ \mathrm { { \Omega } n s }$ of UTC, namely, the National Institute of Standards and Technology (NIST) and the USNO already mentioned. In 1996, the National Physical Laboratory (NPL) in the United Kingdom and the Paris Observatory (OP) could be added to the list. On 27 September 2000,20 out of the $4 6 ~ U T C - U T C ( k )$ published by the BIPM were,in absolute values, less than $1 0 0 \mathrm { n s }$ Table 7.1 illustrates the quality of synchronisation for the four laboratories quoted and for GPS, from January to September 2000.

Table 7.1. Synchronisation between UTC and UTC(k) for four timing laboratories and GPS over the period January to September 2000.   

<table><tr><td>Laboratory or system</td><td>Extremal value of UTC-UTC(k) (ns)</td><td>Mean value of UTC-UTC(k) (ns)</td><td>Rms value of UTC-UTC(k) (ns)</td></tr><tr><td>GPS</td><td>-39</td><td>-7</td><td>13</td></tr><tr><td>NIST</td><td>28</td><td>15</td><td>17</td></tr><tr><td>NPL</td><td>80</td><td>20</td><td>29</td></tr><tr><td>OP</td><td>-49</td><td>-31</td><td>31</td></tr><tr><td>USNO</td><td>-20</td><td>2</td><td>9</td></tr></table>

# 7.4.3 Other forms of atomic time

By convention,TAI is the international reference. However,there is nothing to prevent other time scales being set up using data available the world over, if some advantage is to be gained for specific projects.It might be thought thata more stable and accurate atomic time than TAI would be realised if a longer publication time were possible and if corrections were authorised on the basis of the latest information received.For example, the effect of blackbody radiation on the frequency of primary standards was only taken into account in auniform manner for TAI in September 1995,and no retrospective correction could be made to TAI to improve past values.

We shall see in Chapter 8 that certain shortcomings of TAI are critical in studies that involve timing fast pulsars. Aware of the need for an improved time scale for such studies, the BIPM set up a dated time scale called TT(BIPMxx), where xx represents the two last figures of the year in which it was produced. Although this scale is based on the EAL,data from primary standards is not used in the same way as for TAI.Annual fluctuations,mentioned previously, are eliminated [7.7]. Successive versions of TT(BIPMxx) are not straightforward extensions, since they may differ over the whole length of the time scale from their starting date on 1 January 1977,which is the same for all scales. TT(BIPMxx) is supplied in the form of differences with TAI at standard dates (every ten days, then every five days),upon request to the BIPM. The offset between $T T ( \mathrm { B I P M 9 6 } )$ and $T A I + 3 2 . 1 8 4 ~ \mathrm { s }$ , zero on 1 January 1977,can reach $2 5 ~ \mu \mathrm { s }$

# 7.5 Dissemination of time and frequency

# 7.5.1 Frequency

# (a) Standard frequency emissions

Carrier frequencies of specialised time signal and standard frequency emissions are based on TAI frequency to much greater accuracy than is suggested in ITU recommendations. Most announce uncertainties of $1 0 ^ { - 1 1 }$ , whilst in some cases it is pushed down as far as $1 0 ^ { - 1 2 }$ . The BIPM provides a list of these emissions in the Time Section Annual Report.

Certain other radio signals, used for various purposes, have very accurate frequencies. Loran-C emits at $1 0 0 ~ \mathrm { k H z }$ to within $\pm 1 0 ^ { - 1 2 }$ . Some radio broadcast signals have very accurate frequencies, such as Allouis in France，at $1 6 2 \mathrm { k H z }$ to within $\pm 2 \times 1 0 ^ { - 1 2 }$

These signals cover most frequency reference requirements. They are easily accessed using quite ordinary receivers.

# (b) Access to primary frequency standards

For fundamental metrology, the subject of this book, it is often useful to have access to the frequency of a remote primary frequency standard E. When the greatest possible accuracy is desired, time comparisons are used,as explained in Section 5.6.4a.If A is a local oscillator, $y _ { \mathrm { E } } - y _ { \mathrm { A } }$ is obtained via (5.67) and (5.68).

If time is not a factor, $y _ { \mathrm { E } } - y _ { \mathrm { A } }$ can be obtained without asking anything of the primary laboratory housing E, simply by consulting BIPM publications. These give access to TAI Iocally (e.g., by reception of GPS signals). They also provide, under the notation $d$ ,the relative difference between the duration of the TAI scale unit and the proper second as realised by the standard E,referred to the geoid. We use here the notation $d _ { \mathrm { T A l , E } }$ for this quantity, which is an average over an interval $( T A I _ { 1 } , \ T A I _ { 2 } ) .$ Hence,

$$
[ \langle y _ { \mathrm { E } } \rangle - \langle y _ { \mathrm { T A I } } \rangle ] | _ { \mathrm { g e o i d } } = d _ { \mathrm { T A I , E } } ~ ,
$$

where $\langle \ \rangle$ represents the average over the relevant interval. For the user’s clock A, with proper time $\tau _ { \mathrm { A } }$ ,we measure

$$
N _ { \mathrm { A } } = \frac { \left[ \tau _ { \mathrm { A } } - T A I \right] \left( T A I _ { 2 } \right) - \left[ \tau _ { \mathrm { A } } - T A I \right] \left( T A I _ { 1 } \right) } { T A I _ { 2 } - T A I _ { 1 } } \ ,
$$

and then,by (5.73),

$$
\langle y _ { \mathrm { A } } \rangle - \langle y _ { \mathrm { T A I } } \rangle = N _ { A } + \langle \underline { { { h } } } ( T A I ) \rangle \ .
$$

The function $\underline { { h } }$ is givenby(.3)o(2)anditsaveragevaeistakelog the worldline of A between $T A I _ { 1 }$ and $T A L _ { 2 }$ .Hence,

$$
\langle y _ { \mathrm { A } } - y _ { \mathrm { E } } \rangle = N _ { \mathrm { A } } - d _ { \mathrm { T A I , E } } + \langle \underline { { h } } ( T A I ) \rangle \ .
$$

For a fixed clock A on the Earth, we find

$$
\langle y _ { \mathrm { A } } - y _ { \mathrm { E } } \rangle = N _ { \mathrm { A } } - d _ { \mathrm { T A I , E } } - 1 . 0 9 1 \times 1 0 ^ { - 1 3 } h _ { \mathrm { A } } / \mathrm { k m } ,
$$

where $h _ { \mathrm { { A } } }$ is the altitude of the user above the geoid,in kilometres.

Either by making direct time comparisons or by using BIPM publications, uncertainties involved in accessing primary frequency standards can be significantly less than $1 0 ^ { - 1 4 }$ However standards,where frequencyuncertaitiesarasallas $1 0 ^ { - 1 5 }$ . The problem of how to gain remote access to the frequencies of these standards has not yet been solved.

# 7.5.2 Time

GPS Time is related to TAI by

$$
[ T A I - G P S T i m e ] = 1 9 \mathrm { s } + C 0 \ ,
$$

where the synchronisation discrepancy $C _ { 0 }$ is usually maintained within $\pm 1 0 0$ ns limits.From March 1995 to the present (October 2000),it has remained within these bounds,and has often been below 5O ns. The values of $C _ { 0 }$ are published for each day at $0 \mathrm { h }$ UTC, in BIPM Circular T. Uncertainty is 10 ns.Hence,access to TAI and UTC is possible everywhere to within $\pm 1 0$ ns, although deferred by one or two months, using commercially available GPS time receivers. In order to attain such accuracies,a daily average must be taken over a great many satellite trackings. In addition, coordinates of the antenna must be known to within one or two metres in the WGS84 or ITRF systems. GPS time receivers can give these coordinates, but to insuficient accuracy.

The other highly accurate way of accessing TAI or UTC, once again deferred by one or two months,is to establish a link with some laboratory $k$ whose clocks take part in TAI and for which $U T C - U T C ( k )$ is published. Uncertainties may be slightly less than $1 0 ~ \mathrm { { n s } }$ .This method raises the problem of short range time transfer links. GPS can be used (some errors decreasing with distance),otherwise cable or direct view television represent further possibilities.

Today (2o0O),access through GLONASS has the same qualities as access via GPS. Putting

$$
[ U T C - G L O N A S S ~ T i m e ] = C _ { \mathrm { { 1 } } } ~ ,
$$

values of $C _ { 1 }$ are a few hundred nanoseconds. They are published by the BIPM for each day with uncertainties around $1 0 ~ \mathrm { n s }$

In real time, we may use either the values of UTC transmitted by GPS $\pm 1 0 0$ ns), or a link with a laboratory where $U T C \mathrm { ~ - ~ } U T C ( k )$ can be extrapolated, again with the possibility of uncertainties attaining values around $\pm 1 0 0$ ns.

To lesser accuracy, there are a great many ways of accessing UTC or official time,such as speaking clocks or radio broadcast pips. Some coded emissions can be used to display the time.It is not certain that radio time signals,aimed mainly at navigators,will be able to hold out against the facilities offered by other rapidly developing means of disseminating time and positioning, viz., GPS, GLONASS or their civilian counterparts.

# 7.6 Summary and prospects

The current world organisation of atomic timekeeping was set up at the beginning of the 197Os. At the time,choices were guided by three main considerations.

· There were many caesium atomic clocks in existence, commercially built and possessing excellent long term stability, but falling short in terms of accuracy. Systematic frequency differences persisted throughout the lifetime of these clocks.   
Primary frequency standards only operated on an occasional basis,and doubts remained concerning their stated accuracy.   
· To reduce uncertainties in frequency comparisons due to time comparisons, averaging was required over one or two month periods.

At the beginning of the 198Os, questions were raised about the way atomic time measurement was being organised. The primary standard NRC Cs V at the Canadian National Research Council had been running continuously (as a primary clock) since 1976.It was joined in July 1978 by the German primary clock PTB CS1, and then in 1980 by three other primary clocks at the NRC, viz.,NRC Cs VI A, B and C. There was good frequency agreement between these standards,and the unrivalled accuracy of PTB CS1 $( \pm 3 \times 1 0 ^ { - 1 4 } )$ was confirmed in l986 by PTB CS2, which proved to be even more accurate $( \pm 1 . 5 \times 1 0 ^ { - 1 4 }$ ). These developments made it reasonable to ask whether TAI should not be based directly and solely on such primary clocks. The calculation of TAI from the clock readings of many laboratories was nonetheless maintained,since it guaranteed more reliable results.However,there was another reason,namely,thedesire that TAIsouldremainacollective enterpise, involving the commitment of a significant number of laboratories,both large and small. The number of countries joining the TAI club had grown to thirty by 2000. This spirit of cooperation in the area of time measurement has never failed.Itis through this cooperation that suchclose synchronisations have been possible with UTC,including the synchronisation of GPS which is not required for the system to work, but which simply serves the world community. It is this same spirit that has made it possible to set up time comparison networks that form the very foundation of the whole edifice.

Current research is likely to produce even more accurate and stable primary standards,with uncertainties being decreased by at least a factor of ten. But since 1994,most national timing laboratories have equipped themselves with new commercial caesium clocks in which long term instabilities have also been reduced by a factor of ten, compared with the previous generation of clocks. These instruments are thus progressing at the same rate. However,the accuracy of time comparisons via GPS had made it possible to reduce the frequency sampling period upon which calculation of TAI is based from two months to one month.

Apart from this modification and despite the pressures of progress, the original 197O organisation continues to operate. It is often reassessed by the Consultative Committee for Timeand Frequency but,up to now,the conclusion has always been to leave things as they are.

To conclude, Iet us recall that, today, the time in TAI or UTC can be made available everywhere, to within a hundred nanoseconds in real time, and to within about ten nanoseconds one or two months after the event. Taken as an entity, the second,that is, the duration of one second alone, can be realised at best to within a relative error of about $\pm 5 \times 1 0 ^ { - 1 4 }$ by a cooled caesium atom standard,owing to the short term frequency instability of this device. But this standard can express in seconds a duration of several hours or more to within $1 0 ^ { - 1 5 }$ (relative value). Through access to TAI, the second can be obtainedeverywhere towithinafewmultiplesof $\pm 1 0 ^ { - 1 5 }$ , on average over a few days.

# 8

Astronomical times

Although astronomical times are no longer the best measure of time, they continue to play a role in current research. Universal Time is witness to the Earth's rotation,whilst serving also to establish Coordinated Universal Time (UTC), the practical basis for unifying times the world over. Ephemeris Time (ET) is the best representation of dynamical time before the advent of atomic time in 1955 and is still used to process astronomical observations made prior to that date. And finally, some have hoped that Pulsar Time might exhibit better long term stability than atomic time. In the present chapter, we shall explain how these times are defined,realised and used.

# 8.1 Universal Time

# 8.1.1 Conceptual definition

A historical view of the developments leading up to Universal Time might resemble a series of metamorphoses of apparent solar time (see Section 4.2). It is simpler to give a conceptual definition,based upon the Earth's rotation, which brings out its current role.

There are various forms of Universal Time. The one directly related to the Earth's rotation is UT1. Other forms will be defined in Section 8.1.3.

In Section 3.3.2b, we defined geocentric coordinate systems. One is rotating in space (celestial system) and the other is rotating with the Earth (terrestrial system). The rotation of the terrestrial system with respect to the celestial system is the rotation of the Earth. We showed how these systems are realised as frames of reference ICRF. denoted (C) here, and ITRF, denoted (T) here. It is the rotation of (T) relative to (C) that is described. To do so. we appeal to classical kinematics. The time $\boldsymbol { { \mathit { I } } }$ is treated as absolute and realised by International Atomic Time with negligible uncertainty.

Although three functions of time (the three Euler angles)are suficient to orient (T) with respect to (C),a five parameter representation is preferred, which includes thedirection (I) of therotationaxis.Thelatter moves relative toboth (T) and (C) $^ \dagger$ These parameters are as follows.

· The two angular coordinates giving the position of (I) in (C) describe lunisolar precession-nutation. Observed values are usually given in the form of deviations from a theoretical model of precession-nutation,chosen by convention.At present, deviations from the model are of the order of $0 . 0 1 ^ { \prime \prime }$ They will be reduced to about $0 . 0 0 1 ^ { \prime \prime }$ when a new model adopted in 2000 is put into practice.   
The two angular coordinates of (I) in (T) describe the terrestrial polar motion. They are given in the form of deviations between the direction of (I), this axis being oriented towards the north,and the $X ^ { 3 }$ axis of (T), denoted by $Z$ in IERS publications: $x ( t )$ is measured along the prime meridian and $y ( t )$ along the meridian $9 0 ^ { \circ }$ west. Values of $\chi \left( t \right)$ and $y ( t )$ do not exceed $1 ^ { \prime \prime }$ ， corresponding to $3 0 \mathrm { m }$ on the Earth's surface.   
· An angle $A ( t )$ ,measured around (I),completes the description. The position of (I) is the one it occupies at date $t$ ·

The angle $A$ can be defined in two ways, as we shall see. UT1 is expressed as a function of $A$ by mathematical relations in which numerical parameters are chosen so that, whichever choice is made, the same values of UT1 are obtained. These relations are set up in such a way as to satisfy the following conditions.

(i) The derivative of UT1 with respect to time must be proportional to the modulus of the (variable) rotation vector. Then UT1 fulfills its historical role as a uniform time under the assumption of uniform rotation,and its modern role as a simple representation of the Earth's rotation.   
(ii) The constant of proportionality implied by (i) and the phase are chosen so that,over the millennia, the Sun transits the prime meridian (the Greenwich meridian) at $^ { 1 2 \mathrm { h } }$ UT1, on average.

Strictly speaking, the second condition is not compatible with (i) because,even if the Earth's rotation is uniform, the mean duration of an apparent solar day varies very slowly. However, priority has been given to (i),and condition (i)

is only approximately fulfiled. The shift between UT1 and the alternation of day and night resulting from this approximation is quite negligible, being well under one second over a few centuries.

If the Earth’s rotation vector is $\omega ( t )$ with length $\omega ( t )$ , we must therefore have

$$
\frac { \mathrm { d } \left( U T I \right) } { \mathrm { d } t } = \frac { \omega ( t ) } { \omega _ { 0 } } \ , \ \cdot
$$

where $\omega _ { 0 }$ is a constant angular speed corresponding to $\mathrm { d } \left( U T I \right) = \mathrm { d } t$ ,whose value is chosen to satisfy (ii). In integral form, this means that

$$
[ U T I ] ( t ) = [ U T I ] ( t _ { 0 } ) + \frac { 1 } { \omega _ { 0 } } \int _ { t _ { 0 } } ^ { t } \omega ( t ) \mathrm { d } t \mathrm { ~ , ~ }
$$

the constant of integration also being chosen to satisfy (ii).

Equation (8.2) expresses the conceptual definition of UT1, whilst the relationships between the two forms of $A$ and UT1 given in Section 8.1.2 are practical definitions.

Let us review some other useful relations. As the values of UT1 are published in the form of corrections to TAI, as a function of the TAI (or UTC) date,it is sometimes convenient to write (8.2) in the form:

$$
[ U T I - T A I ] ( t ) = [ U T I - T A I ] ( t _ { 0 } ) + \int _ { t _ { 0 } } ^ { t } \frac { \Delta \omega ( t ) } { \omega _ { 0 } } \mathrm { d } t \ ,
$$

where $\Delta \omega = \omega - \omega _ { 0 }$

The quantity $\omega ( t )$ can be deduced from published values of $\ U T I - T A I$ by

$$
\omega ( t ) = \left[ 1 + \frac { \mathrm { d } ( U T I - T A I ) } { \mathrm { d } ( T A I ) } \right] \omega _ { 0 } .
$$

Instead of $\omega _ { 0 }$ , it is common to use a more suggestive quantity $D ( t )$ , called the lengthofdaiistioinseit increase in UT1. Then,

$$
D ( t ) = \frac { \omega _ { 0 } } { \omega ( t ) } \times 8 6 4 0 0 \mathrm { ~ s ~ } .
$$

# 8.1.2 Practical definition of UT1

We shall now tackle the subtle problem of defining the directions between which the angle $A ( t )$ is measured,distinguishing two options.

![](images/7b4a22cb98eb7c0435c73b58e41bc082ed47e7185027ca7d4e99c34e5ab82d38.jpg)  
Fig.8.1. Defining the instantaneous longitude origin $\Omega$ in the moving equator.

# (a) Use of non-rotating origins

A form $A _ { \mathrm { S } } ( t )$ of $A ( t )$ , sometimes called the stellar angle, has recently been found whereby this angle is linearly related to UT1 [8.1, 8.2].

Following the method generally used by astronomers, we represent directions by straight lines originating in some arbitrarily chosen point O. These lines intersect a sphere of unit radius (the celestial sphere) in points that can be taken to represent these directions. The equator is a great circle on this sphere and $A _ { S } ( t )$ is represented by an arc on the equator at date $t$

Let us begin with the determination of the origin of $A _ { \mathrm { S } } ( t )$ in (T). To simplify, we assume that the $X ^ { 3 }$ axis corresponds to the position $\mathrm { P _ { 0 } }$ of the pole at date $t _ { 0 }$ .Let $\Omega _ { 0 }$ be the origin for longitudes in (T),i.e., the point representing $X ^ { 1 }$ At date $t$ , the pole has moved to $\mathrm { P }$ along the trajectory C (see Figure 8.1). The equator of P cuts the one associated with $\mathrm { P _ { 0 } }$ at $_ \mathrm { N }$ (the ascending node). In order to position the instantaneous longitude origin $\Omega$ ,the following condition is imposed: the rectangular triad attached to OP and $\mathrm { O } \Omega$ has no instantaneous component of rotation about OP when P moves. If P is located via its polar coordinates as shown in Figure 8.1, it is easy to show that the quantity $s =$ $\Omega N - \Omega _ { 0 } N$ is given by

$$
s = \int _ { C } ( \cos d - 1 ) \mathrm { d } E \ .
$$

The position of $\Omega$ thus depends on the whole history of the Earth's rotation,a worrying but unavoidable conclusion. In this case, $s$ is small, because $d$ never exceeds $1 ^ { \prime \prime }$ .This is fortunate,because $\boldsymbol { \mathcal { S } }$ has always been taken as zero in practice. The situation is quite different in (C).

When treated in (C), the same problem leads us to define an origin in the moving equator, called the non-rotating origin o. However, the motion of P in(C) includes a secular term (precession) of about $2 0 ^ { \prime \prime }$ per year and periodic terms (nutation) with total amplitude around $2 0 ^ { \prime \prime }$ , in such a way that $s$ can take on significant values. For example, for precession we find

$$
s _ { \mathrm { P } } = 3 6 . 2 8 ^ { \prime \prime } ( t - t _ { 0 } ) ^ { 3 } - 0 . 0 4 ^ { \prime \prime } ( t - t _ { 0 } ) ^ { 4 } + \cdot \cdot \cdot \ ,
$$

where $t \ : - \ : t _ { 0 }$ is measured in thousands of years. The full expression for $s$ includingprecessoadtaioalidtoitinwi $1 0 ^ { - 6 ^ { \prime \prime } }$ until 2100, is given in [8.3].

Having established the origins $\Omega$ and $\sigma$ , we can define $A _ { \mathrm { S } } ( t )$ modulo $2 \pi$ as the arc $\Omega \sigma$ . Since every component of rotation about the polar axis is zero by definition of the non-rotating origins, $A _ { \mathrm { S } } ( t )$ represents the integral in (8.2) directly. The values of UT1 are proportional to $A _ { S }$ . It is useful to deduce the relation between UT1 and $A _ { \mathrm { S } }$ from the expression for $A _ { \mathrm { S } }$ at $0 \mathrm { ~ h ~ U T 1 }$ ,as provided each day. Let $d _ { \mathrm { u } } ^ { \prime }$ be the number of UT1 days elapsed since 20oo January 1 at $1 2 \mathrm { ~ h ~ U T 1 }$ ( $\mathrm { i } d _ { \mathrm { u } } ^ { \prime }$ is a positive or negative whole number plus or minus 0.5). Then setting $T _ { \mathrm { u } } ^ { \prime } = d _ { \mathrm { u } } ^ { \prime } / 3 6 5 2 5$ (expressed in Julian centuries of 36 525 days) and taking one second of hour angle, viz., $1 5 ^ { \prime \prime }$ ,as unit of angle,a common practice amongst astronomers,we have

$$
A _ { \mathrm { S } } { \mathrm { ~ a t ~ } } 0 { \mathrm { ~ h ~ } } \mathrm { U T } 1 = 2 4 1 1 0 . 5 4 8 4 1 + 8 6 3 9 8 7 7 . 3 1 7 3 8 T _ { \mathrm { u } } ^ { \prime } .
$$

This equation is established using the value of $\omega _ { 0 }$ given by

$$
\omega _ { 0 } = 7 . 2 9 2 1 1 5 1 4 6 7 0 6 \times 1 0 ^ { - 5 } \mathrm { r a d s ^ { - 1 } } ,
$$

chosen so as to satisfy the conceptual definition of UT1.

To obtain $A _ { S }$ at a general instant of time, $d _ { \mathrm { u } }$ must be calculated in the same way as $d _ { \mathrm { u } } ^ { \prime }$ , but in UTl days and fractions ofa day for this instant, together with the corresponding $T _ { \parallel }$ ,adding $8 6 4 0 0 \times 3 6 5 2 5$ seconds to the coeficients of $T _ { \mathrm { u } } ^ { \prime }$ For example, with $A _ { S }$ in revolutions,

$$
A _ { \mathrm { S } } = 0 . 7 7 9 0 5 7 2 7 3 2 6 4 + 1 . 0 0 2 7 3 7 8 1 1 9 1 1 3 5 4 d _ { \mathrm { u } } .
$$

At its General Assembly in 2000,the IAU recommended the use of the non-rotating origins associated with the Celestial Intermediate Pole, under the names of Celestial Ephemeris Origin in (C) and Terrestrial Ephemeris Origin in (T). This recommendation should take effect in 2003.