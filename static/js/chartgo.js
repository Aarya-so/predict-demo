function jsFunction(value)
{
    //alert(value);

    fetch("/get_pie_data?district=" + value)  // Change district dynamically
    .then(response => response.json())
    .then(data => {
        
        //if (document.getElementById("results-graph"))
        //{
        //    console.log("innn");
        //    document.getElementById("results-graph").remove(); // this is my <canvas> element
        //}
        //document.getElementById("demo").append('<canvas id="results-graph"><canvas>');
        //canvasobj = document.querySelector('#results-graph');
        
        
        
        var ctx = document.getElementById("results-graph").getContext("2d");
        
        new Chart(ctx, {
            type: "pie",
            data: {
                labels: data.labels,
                datasets: [{
                    data: data.values,
                    backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"]
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' },
                    title: { display: true, text: 'Top 5 Commodities by Arrivals' }
                }
            }
        });
    })
    .catch(error => console.error("Error fetching data:", error));
    

    /*let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/get_pie_data?district=" + value, false);
    xhttp.send();

    
  var data = xhttp.responseText;  
            var ctx = document.getElementById("cropPieChart").getContext("2d");
            new Chart(ctx, {
                type: "pie",
                data: {
                    labels: data.labels,
                    datasets: [{
                        data: data.values,
                        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"]
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'top' },
                        title: { display: true, text: 'Top 5 Commodities by Arrivals' }
                    }
                }
            }); */
    

    //document.getElementById("demo").innerHTML = xhttp.responseText;
}
/*document.addEventListener("DOMContentLoaded", function() {
    fetch("/get_pie_data?district=Kinnaur")  // Change district dynamically
        .then(response => response.json())
        .then(data => {
            var ctx = document.getElementById("cropPieChart").getContext("2d");
            new Chart(ctx, {
                type: "pie",
                data: {
                    labels: data.labels,
                    datasets: [{
                        data: data.values,
                        backgroundColor: ["#FF6384", "#36A2EB", "#FFCE56", "#4BC0C0", "#9966FF"]
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: { position: 'top' },
                        title: { display: true, text: 'Top 5 Commodities by Arrivals' }
                    }
                }
            });
        })
        .catch(error => console.error("Error fetching data:", error));
});*/
