file = "/var/www/html/Dallas-County-Covid19-API/CovidList.csv"
set datafile separator ","
set datafile missing "NaN"

set xdata time
set timefmt "%m/%d/%y"

set grid x
set key box opaque
set style textbox opaque
set key top left reverse Left

set terminal png size 1024,768 
set output "/var/www/html/covidgraph.png"
plot file using 1:2 tit "Confirmed Cases" w linespoints lw 3 pt 12, \
file	  using 1:2:2 with labels center boxed offset .5,1 notitle, \
file 	  using 1:3 tit "Deaths" w linespoints lw 3 pt 12, \
file	  using 1:3:3 with labels center boxed offset .5,1 notitle

