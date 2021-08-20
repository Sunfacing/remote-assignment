url = 'http://13.230.176.178:4000/api/1.0/remote-w4-data'
btn = document.getElementById('load')


// Solution 1 - Most Basic 


function ajax(src, callback){
    callback(src);
}


function render(url){
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            var items = JSON.parse(xhr.responseText);
            var ul = document.createElement('ul');
            for (var i=0; i < items.length; i++) {
                li = document.createElement('li');
                li.className = 'product'
                li.innerHTML = 'Product: ' + items[i].name 
                               + '<br> Price: ' 
                               + items[i].price 
                               + '<br> Description: '
                               + items[i].description;
                ul.appendChild(li);
            }
            document.getElementById('products').append(ul);
        }
    }   
    xhr.open('GET', url);
    xhr.send();
};


btn.addEventListener('click', (event)=>{
    ajax(url, function(response){
        render(response);
    })    
    event.target.remove()
})
 



// Solution 2 - Use Promise with fetch

// function render(productList){
//     var ul = document.createElement('ul');
//     productList.map( product => {
//         var li = document.createElement('li');
//         li.className = 'product';
//         li.innerHTML = 'Product: ' + product.name
//                         + '<br> Price: ' 
//                         + product.price 
//                         + '<br> Description: '
//                         + product.description;
//         ul.appendChild(li);
//     })
//     document.getElementById('products').append(ul);
// };
        


// fetch(url)
//     .then( response => response.json())
//     .then(render)
//     .finally(() => alert('Hey'))




// Solution 3 - Use Async/Await && add a button

// async function getJSON(url) {
//     const response = await fetch(url);
//     const data = await response.json();
//     return data
// };

// async function render(productList){
//     var ul = document.createElement('ul');
//     productList.map( async(product) => {
//         var li = document.createElement('li');
//         li.className = 'product';
//         li.innerHTML = 'Product: ' + product.name
//                         + '<br> Price: ' 
//                         + product.price 
//                         + '<br> Description: '
//                         + product.description;
//         ul.appendChild(li);
//     })
//     document.getElementById('products').append(ul);
// };


// btn.addEventListener('click', (event) => {
//     event.target.textContent = "Loading...";
//     getJSON(url)
//         .then(render)
//         .finally(event.target.remove())
// })