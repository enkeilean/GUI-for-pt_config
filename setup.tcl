set DESIGN 1


set generate_ice 2
set generate_redhawk 3


set verilog_file 4


set spefDir 5
if {[regexp rcworstm40c $corner]} {
  set spef_file $spefDir/qrcRCWM40C.spef.gz
} elseif {[regexp rcworst125c $corner]} {
  set spef_file $spefDir/qrcRCW125C.spef.gz
} elseif {[regexp cworstm40c $corner]} {
  set spef_file $spefDir/qrcCWM40C.spef.gz
} elseif {[regexp cworst125c $corner]} {
  set spef_file $spefDir/qrcCW125C.spef.gz
} elseif {[regexp rcbestm40c $corner]} {
  set spef_file $spefDir/qrcRCBM40C.spef.gz
} elseif {[regexp rcbest125c $corner]} {
  set spef_file $spefDir/qrcRCB125C.spef.gz
} elseif {[regexp cbestm40c $corner]} {
  set spef_file $spefDir/qrcCBM40C.spef.gz
} elseif {[regexp cbest125c $corner]} {
  set spef_file $spefDir/qrcCB125C.spef.gz
} else {
  set spef_file $spefDir/qrcTYP25C.spef.gz
}



set sdcDir 6
if {[regexp func $mode]} {
set sdc_file $func_sdcDir/FunDft_flattensdc.tcl
} elseif {[regexp b $mode]} {
    set sdc_file $func_sdcDir/2
} elseif {[regexp c $mode]} {
    set sdc_file $func_sdcDir/3

}