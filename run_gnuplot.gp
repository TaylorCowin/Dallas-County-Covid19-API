file = "/var/www/html/CovidList.csv"

set datafile separator ","
set datafile missing "NaN"

set xdata time
set timefmt "%m/%d/%Y"
#set format x "%m/%d"

#set xtics 1 
#set format mxtics "%m/%d"
#set logscale y

set grid x
set grid y
set grid mxtics xtics

set key box opaque
set style textbox opaque
set key top left reverse Left

set terminal png size 1024,768 
set output "/var/www/html/covidgraph.png"
plot file using 1:2 tit "Confirmed Cases" w linespoints lw 3 pt 12, \
file	  using 1:2:2 with labels center boxed offset 3.5,0 notitle, \
file 	  using 1:3 tit "Deaths" w linespoints lw 3 pt 12, \
file	  using 1:3:3 with labels center boxed offset 1,1.5 notitle

