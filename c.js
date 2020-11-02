d3.csv("./CovidList.csv").then(makeChart);

function makeChart(data) {
    if (data.length == 0) {
        console.log(data.length);
    }
    for (let x of data) {
        console.log(x);
    }

    var ctx = document.getElementById("chart").getContext("2d");
    var dates = data.map(function (d) {
        return d.Date;
    });
    var cases = data.map(function (d) {
        return d.Cases;
    });
    var deaths = data.map(function (d) {
        return d.Deaths;
    });

    let lastDate = dates[dates.length-1];
    let lastCases = cases[cases.length-1];
    let lastDeaths = deaths[deaths.length-1];
    let stringOut = lastDate + ": " + lastCases.toString().fontcolor("#9e3dff") + " cases, " + lastDeaths.toString().fontcolor("#ff943d") + " deaths";
    document.getElementById("lastcounts").innerHTML = stringOut;

    var myChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: dates,
            datasets: [
                {
                    label: "Covid-19 Cases",
                    data: cases,
                    borderColor: "rgb(158, 61, 255)",
                    borderWidth: 2,
                    pointRadius: 1,
                },
                {
                    label: "Covid-19 Deaths",
                    data: deaths,
                    borderColor: "rgb(255, 148, 61)",
                    borderWidth: 2,
                    pointRadius: 1,
                },
            ],
        },
        options: {
            responsive: true,
            tooltips: {
                mode: 'index',
                intersect: false,
            },
            legend: {
                display: false,
                labels: {
                    fontColor: "white",
                }
            },
            scales: {
                xAxes: [{
                    display: true,

                    ticks: {
                        fontColor: "white",
                        fontSize: 14
                    }
                }],
                yAxes: [{
                    display: true,

                    ticks: {
                        fontColor: "white",
                        fontSize: 14
                    }
                }],

            }
        },
    });
}