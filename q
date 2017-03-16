AMIXER(1)                   General Commands Manual                  AMIXER(1)



NNAAMMEE
       amixer - command-line mixer for ALSA soundcard driver

SSYYNNOOPPSSIISS
       aammiixxeerr [_-_o_p_t_i_o_n] [_c_m_d]

DDEESSCCRRIIPPTTIIOONN
       aammiixxeerr  allows command-line control of the mixer for the ALSA soundcard
       driver.  aammiixxeerr supports multiple soundcards.

       aammiixxeerr with no arguments will display the current  mixer  settings  for
       the  default  soundcard and device. This is a good way to see a list of
       the simple mixer controls you can use.


CCOOMMMMAANNDDSS
       _h_e_l_p   Shows syntax.


       _i_n_f_o   Shows the information about a mixer device.


       _s_c_o_n_t_r_o_l_s
              Shows a complete list of simple mixer controls.


       _s_c_o_n_t_e_n_t_s
              Shows a complete list of simple mixer controls with  their  con‐
              tents.


       _s_e_t or _s_s_e_t <_S_C_O_N_T_R_O_L> <_P_A_R_A_M_E_T_E_R> ...
              Sets the simple mixer control contents. The parameter can be the
              volume either as a percentage from 0% to 100% with _%  suffix,  a
              dB  gain  with  _d_B  suffix  (like -12.5dB), or an exact hardware
              value.  The dB gain can be used only for the mixer elements with
              available  dB  information.   When plus(+) or minus(-) letter is
              appended after volume value, the volume is incremented or decre‐
              mented from the current value, respectively.

              The  parameters  _c_a_p_,  _n_o_c_a_p_,  _m_u_t_e_,  _u_n_m_u_t_e_, _t_o_g_g_l_e are used to
              change capture (recording) and muting for the group specified.

              The optional modifiers can be put as extra parameters to specify
              the  stream direction or channels to apply.  The modifiers _p_l_a_y_‐
              _b_a_c_k and _c_a_p_t_u_r_e specify the stream, and  the  modifiers  _f_r_o_n_t_,
              _r_e_a_r_, _c_e_n_t_e_r_, _w_o_o_f_e_r are used to specify channels to be changed.

              A simple mixer control must be specified. Only one device can be
              controlled at a time.


       _g_e_t or _s_g_e_t <_S_C_O_N_T_R_O_L>
              Shows the simple mixer control contents.

              A simple mixer control must be specified. Only one device can be
              controlled at a time.


       _c_o_n_t_r_o_l_s
              Shows a complete list of card controls.


       _c_o_n_t_e_n_t_s
              Shows a complete list of card controls with their contents.


       _c_s_e_t <_C_O_N_T_R_O_L> <_P_A_R_A_M_E_T_E_R> ...
              Sets  the card control contents. The identifier has these compo‐
              nents: iface, name, index, device, subdevice,  numid.  The  next
              argument specifies the value of control.


       _c_g_e_t <_C_O_N_T_R_O_L>
              Shows  the card control contents. The identifier has same syntax
              as for the _c_s_e_t command.


OOPPTTIIOONNSS
       _-_c card

              Select the card number to control. The device name created  from
              this  parameter has syntax 'hw:N' where N is specified card num‐
              ber.


       _-_D device

              Select the device name to control. The default control  name  is
              'default'.


       _-_s | _-_-_s_t_d_i_n

              Read  from  stdin  and  execute the command on each line sequen‐
              tially.  When this option is given, the command in  command-line
              arguments is ignored.

              Only  sset  and  cset are accepted.  Other commands are ignored.
              The commands to unmatched ids are ignored without errors too.


       _-_h     Help: show syntax.


       _-_q     Quiet mode. Do not show results of changes.


       _-_R     Use the raw value for evaluating the percentage  representation.
              This is the default mode.


       _-_M     Use  the mapped volume for evaluating the percentage representa‐
              tion like aallssaammiixxeerr, to be more natural for human ear.


EEXXAAMMPPLLEESS
       aammiixxeerr --cc 11 sssseett LLiinnee,,00 8800%%,,4400%% uunnmmuuttee ccaapp
              will set the second soundcard's left line input  volume  to  80%
              and  right  line  input  to  40%,  unmute it, and select it as a
              source for capture (recording).


       aammiixxeerr --cc 11 ---- sssseett MMaasstteerr ppllaayybbaacckk --2200ddBB
              will set the master volume of the second card to -20dB.  If  the
              master  has  multiple channels, all channels are set to the same
              value.


       aammiixxeerr --cc 11 sseett PPCCMM 22ddBB++
              will increase the PCM volume of the second card with 2dB.   When
              both playback and capture volumes exist, this is applied to both
              volumes.


       aammiixxeerr --cc 22 ccsseett iiffaaccee==MMIIXXEERR,,nnaammee==''LLiinnee PPllaayybbaacckk VVoolluummee"",,iinnddeexx==11 4400%%
              will set the third soundcard's second line playback volume(s) to
              40%


       aammiixxeerr --cc 22 ccsseett nnuummiidd==3344 4400%%
              will set the 34th soundcard element to 40%


SSEEEE AALLSSOO
        aallssaammiixxeerr((11))


BBUUGGSS
       None known.


AAUUTTHHOORR
       aammiixxeerr  is  by  Jaroslav  Kysela <perex@perex.cz>.  This document is by
       Paul Winkler <zarmzarm@erols.com> and Jaroslav Kysela <perex@perex.cz>.



                                  11 Aug 2000                        AMIXER(1)
