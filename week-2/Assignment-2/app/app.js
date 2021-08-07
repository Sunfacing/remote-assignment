const bgImg = document.querySelector('img.background_img');
const barPrompt = document.querySelector('.search_bar_prompt');
let i = 0 // to select welcome sentence in a list, i changes every time user clicks the banner
const recDiv = document.querySelector('div.recommandation#activity');
const explore = document.querySelector('button.section_head.section_button');



// change welcome sectence on the banner
let intro = [
    'Your Next destination',
    'Search to start your itinerary',
    'A place you always want to go',
    'Don\'t wait, search now'
]


bgImg.addEventListener('click', () => {
    barPrompt.textContent = intro[( i + 1 ) % intro.length];
    i ++;
})



// hide recommandation section first time browsing, and display when 'Explore More' is clicked
recDiv.style.display = 'none';
explore.addEventListener('click', () => {
    if (recDiv.style.display == 'none') {
        recDiv.style.display = 'block';
        explore.textContent = '- Hide';
    } else {
        recDiv.style.display = 'none';
        explore.textContent = '+ Explore More';
    } 
})
