
let arr = []
let datas = []
for (let i = 0; i < 9500; i++) {
    datas.push(i)
}
for (let i = 0; i < datas.length; i++) {
    arr.push(i)
}
let min, max
if (arr.length >= 1000) {
    console.log("true")
    min = arr.length - 1000,
        max = arr.length
}
else {
    console.log("false")
    min = 0,
        max = arr.length
}

$('#container').highcharts({
    chart: {
        backgroundColor: '#f1f2f6',
        type: 'line',
        marginLeft: 100,
        marginRight: 100
    },
    legend: {
        symbolHeight: 8,
        symbolWidth: 8,
        symbolRadius: 4,
        margin: 15,
        backgroundColor: '#FFFFFF',
        layout: 'horizontal',
        itemDistance: 25,
        symbolMargin: 10,
        itemStyle: {
            color: 'black',
            fontWeight: 'normal'
        }
    },
    title: {
        text: ''
    },
    xAxis: {
        categories: arr,
        min: min,
        max: max
    },
    yAxis: {
        min: 0,
        title: {
            text: ''
        }
    },

    series: [{
        name: 'Sales',
        data: datas,
        color: '#ff0000'

    },]
}, function (chart) { // on complete
    function noop() { };
    chart.renderer.button('<', chart.plotLeft - 60, chart.plotHeight - 135 + chart.plotTop, noop).addClass('left').add();


    chart.renderer.button('>', chart.plotLeft + chart.plotWidth + 10, chart.plotHeight + chart.plotTop - 135, noop).addClass('right').add();

    $('.left').click(function () {
        let { min, max, dataMin } = chart.xAxis[0].getExtremes()
        console.log("left", min, max, dataMin)
        if (min - 1000 >= dataMin) {
            min -= 1000
            max -= 1000
        }
        else if (min - 1000 < dataMin) {
            min = 0
            max = 1000
        }
        chart.xAxis[0].setExtremes(min, max)
    });
    $('.right').click(function () {
        let { min, max, dataMax } = chart.xAxis[0].getExtremes()
        console.log("right", min, max, dataMax)
        
        if (max + 1000 <= dataMax) {
            min += 1000
            max += 1000
        }
        else if(max==arr.length){
          

        }
        else if (max + 1000 > dataMax) {
            console.log("i am max", max)
            min = max
            max = arr.length
        }
        
        chart.xAxis[0].setExtremes(min, max)
    })
});

//  movechart plugib block
    // const options = {
    //   chart: {
    //     type: 'line',
    //     panning: true,
    //     events: {
    //       load: function () {
    //         const chart = this
    //         const moveLeft = () => {
    //           let { min, max, dataMin } = chart.xAxis[0].getExtremes()
    //           if (min - 1000 >= dataMin) {
    //             min -= 1000
    //             max -= 1000
    //           }
    //           chart.xAxis[0].setExtremes(min, max)
    //         }
    //         const moveRight = () => {
    //           let { min, max, dataMax } = chart.xAxis[0].getExtremes()
    //           if (max + 1000 <= dataMax) {
    //             min += 1000
    //             max += 1000
    //           }
    //           chart.xAxis[0].setExtremes(min, max)
    //         }
    //         const leftArrowUrl = 'https://www.svgrepo.com/show/238491/left-arrow-next.svg'
    //         const rightArrowUrl = 'https://www.svgrepo.com/show/67470/right-arrow.svg'
    //         const leftArrow = chart.renderer.image(leftArrowUrl, 0, 150, 30, 30).attr({ zIndex: 10 })
    //         const rightArrow = chart.renderer.image(rightArrowUrl, 800, 150, 30, 30).attr({ zIndex: 10 })
    //         leftArrow.on('click', moveLeft).add()
    //         rightArrow.on('click', moveRight).add()
    //       }
    //     }
    //   },
    //   title: {
    //     text: 'Contains 2000 Data'
    //   },
    //   subtitle: {
    //     text: 'Scrolls by 1000 Data'
    //   },
    //   plotOptions: {
    //     series: {
    //       lineWidth: 1,
    //       stickyTracking: false

    //     }
    //   },
    //   credits: {
    //     enabled: false
    //   },
    //   xAxis: {
    //     categories: arr,
    //     min: arr.length - 1000,
    //     max: arr.length
    //   },
    //   yAxis: {
    //     title: {
    //       text: '·'
    //     }
    //   },
    //   series: [{
    //     name: 'Date',
    //     data: datas,
    //     states: {
    //       hover: {
    //         enabled: false
    //       }
    //     },
    //   }],
    //   exporting: {
    //     enabled: false
    //   },

    // }
    // const chart = Highcharts.chart('container', options);