# Data Exploration

## Solar Winds
According to Ovationpyme it's the variables:
```
Bx='BX_GSE',
By='BY_GSM',
Bz='BZ_GSM',
V=velvar,
Ni=densvar
```
If hourly data is chosen the "V" and "N" else it's "flow_speed" and "proton density"

Ovation Pyme calculates Newell Coupling

Ovation Pyme reads date in Julian datetime using special_datetime.datetimearr2jd

From our assumption it calculates a weighted average sum from a solar wind calc getting seasonal flux from that

For every season a different estimation of the Flux is done 

Two challenges: Flux computation and Gridding of the Flux

There are four types of auroras: Diffusive (split in diffusive ions and electrons), Monoenergetic and Broadband

Task: Extract Datasets (Labels) on OvationPyme

###