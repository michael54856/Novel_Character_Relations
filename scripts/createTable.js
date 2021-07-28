

let nodeBtn = document.getElementById("nodeButton");
nodeBtn.addEventListener("click", function(){
    let tableContainer = document.getElementById("myTable");
    let tableHTML = "<table><thead><tr><th>名次</th><th>人物</th><th>重要程度</th></tr></thead>";
    $.getJSON( "../data.json", function(data)
    {
        tableHTML += "<tbody>";
        $.each(data["nodes"],function(i,item)
        {

            tableHTML += "<tr>";
            tableHTML += "<td>"+(i+1)+"</td>";
            tableHTML += "<td>"+item["id"]+"</td>";
            tableHTML += "<td>"+item["val"]+"</td>";
            tableHTML += "</tr>"; 
        }); 
        tableHTML += "</tbody>";
        tableHTML += "</table>";
        tableContainer.innerHTML = tableHTML;
    });
    
});

let edgeBtn = document.getElementById("edgeButton");
edgeBtn.addEventListener("click", function(){
    let tableContainer = document.getElementById("myTable");
    let tableHTML = "<table><thead><tr><th>名次</th><th>人物(1)</th><th>人物(2)</th><th>關聯次數</th></tr></thead>";
    $.getJSON( "../data.json", function(data)
    {
        tableHTML += "<tbody>";
        $.each(data["links"],function(i,item)
        {

            tableHTML += "<tr>";
            tableHTML += "<td>"+(i+1)+"</td>";
            tableHTML += "<td>"+item["source"]+"</td>";
            tableHTML += "<td>"+item["target"]+"</td>";
            tableHTML += "<td>"+item["val"]+"</td>";
            tableHTML += "</tr>"; 
        }); 
        tableHTML += "</tbody>";
        tableHTML += "</table>";
        tableContainer.innerHTML = tableHTML;
    });
});
