function wordcloud(text) {
    anychart.onDocumentReady(function () {
        console.log("prout");
        console.log(text);
        // code to create a word cloud chart will be here
        var data = text;
        console.log(data);


        // create a tag (word) cloud chart
        var chart = anychart.tagCloud(data);

        // set a chart title
        chart.title('Wordcloud')
        // set an array of angles at which the words will be laid out
        chart.angles([0])
        // enable a color range
        chart.colorRange(true);
        // set the color range length
        chart.colorRange().length('80%');

        // display the word cloud chart
        chart.container("containerr");
        chart.draw();
    });
}