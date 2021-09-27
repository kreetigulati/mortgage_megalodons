// // Getting a reference to the button on the page with the id property set to `click-me`
// var button = d3.select("#click-me");

// // This function is triggered when the button is clicked
// function handleClick() {
//     d3.event.preventDefault();
//     // console.log(document.getElementById("input-debtratio").value);

//     // find the respective encoded value based on the input that the user selects (categorical values)
//     d3.json("static/json/combined_encoded.json", function(data) {
//         // console.log(data);
//         // console.log(data.debt_to_income_ratio);

//         // debt to income ratio
//         var count_debt = Object.keys(data.debt_to_income_ratio).length;
//         // console.log(count);
//         for (var i = 0; i < count_debt; i++) {
//         if (document.getElementById("input-debtratio").value == data.debt_to_income_ratio[i]) {encoded_debt = data.encoded_debt_ratio[i]};
//         };
//         console.log(document.getElementById("input-debtratio").value)
//         console.log(encoded_debt);
        
//         // // applicant age
//         // var count_appage = Object.keys(data.applicant_age).length;
//         // // console.log(count);
//         // for (var i = 0; i < count_appage; i++) {
//         // if (document.getElementById("input-appage").value == data.applicant_age[i]) {encoded_appage = data.encoded_applicant_age[i]};
//         // };
//         // console.log(document.getElementById("input-appage").value)
//         // console.log(encoded_appage);

//         // // co-applicant age
//         // var count_coappage = Object.keys(data.co_applicant_age).length;
//         // // console.log(count);
//         // for (var i = 0; i < count_coappage; i++) {
//         // if (document.getElementById("input-coappage").value == data.co_applicant_age[i]) {encoded_coappage = data.encoded_co_applicant_age[i]};
//         // };
//         // console.log(document.getElementById("input-coappage").value)
//         // console.log(encoded_coappage);

//         // // conforming loan limit
//         // var count_limit = Object.keys(data.conforming_loan_limit).length;
//         // // console.log(count);
//         // for (var i = 0; i < count_limit; i++) {
//         // if (document.getElementById("input-limit").value == data.conforming_loan_limit[i]) {encoded_limit = data.encoded_loan_limit[i]};
//         // };
//         // console.log(document.getElementById("input-limit").value)
//         // console.log(encoded_limit);

//         // // derived dwelling category
//         // var count_dwelling = Object.keys(data.derived_dwelling_category).length;
//         // // console.log(count);
//         // for (var i = 0; i < count_dwelling; i++) {
//         // if (document.getElementById("input-dwelling").value == data.derived_dwelling_category[i]) {encoded_dwelling = data.encoded_dwelling_category[i]};
//         // };
//         // console.log(document.getElementById("input-dwelling").value)
//         // console.log(encoded_dwelling);

//         // // state code
//         // var count_state = Object.keys(data.state_code).length;
//         // // console.log(count);
//         // for (var i = 0; i < count_state; i++) {
//         // if (document.getElementById("input-state").value == data.state_code[i]) {encoded_state = data.encoded_state_code[i]};
//         // };
//         // console.log(document.getElementById("input-state").value)
//         // console.log(encoded_state);
        
//         // open dashboard browser


//     });

//     d3.csv("static/data/encoded_mortgage2.csv", function(csv) {
//         csv_filtered = csv.filter(function(row) {
//             return row['loan_amount'] > document.getElementById("input-loan").value});
        
//             // console.log(document.getElementById("input-loan").value)
//         percent_amount = ((csv.length-csv_filtered.length)/csv.length)*100;
//         var max = d3.max(csv, function(d) { return d.loan_amount; });
//         console.log(max);
//         console.log(percent_amount);

//         var data = [
//         {
//             domain: { x: [0, 1], y: [0, 1] },
//             value: percent_amount,
//             title: { text: "Loan Amount Requested: " + document.getElementById("input-loan").value},
//             type: "indicator",
//             mode: "gauge+number",
//             delta: { reference: percent_amount},
//             gauge: { axis: { range: [null, 100] } }
//         }
//         ];

//         var layout = { width: 600, height: 400 };
//         Plotly.newPlot('plot', data, layout);
//             });
// }
// // We can use the `on` function in d3 to attach an event to the handler function
// button.on("click", handleClick)