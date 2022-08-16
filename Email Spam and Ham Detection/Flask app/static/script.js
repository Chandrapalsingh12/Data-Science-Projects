function getVal() {
    const val = document.getElementById('inputs'). value;
    if(val === 1){
        
    }
    console.log(val)
}
console.log("hello");


const input_zone = document.querySelector("#input"),
  emoji = document.querySelector(".emoji"),
  emojis_list = {
    grinning: "&#128513;",
    laugh: "&#128514;",
    happy: "&#128515;",
    oops: "&#128517;",
    haha: "&#128518;",
    angel: "&#128519;",
    evil: "&#128520;",
    winking: "&#128521;",
    blushing: "&#128522;",
    yummy: "&#128523;",
    relieved: "&#128524;",
    loved: "&#128525;",
    cool: "&#128526;",
    smirking: "&#128527;",
    neutral: "&#128528;",
    expressionless: "&#128529;",
    unamused: "&#128530;",
    sweat: "&#128531;",
    pensive: "&#128532;",
    confused: "&#128533;",
    confounded: "&#128534;",
    kissing: "&#128535;",
    kiss: "&#128536;",
    smooch: "&#128538;",
    tongue: "&#128540;",
    insane: "&#128541;",
    sad: "&#128542;",
    "worried ": "&#128543;",
    angry: "&#128544;",
    pouting: "&#128545;",
    crying: "&#128546;",
    persevering: "&#128547;",
    pissed: "&#128548;",
    upset: "&#128549;",
    frowning: "&#128550;",
    anguished: "&#128551;",
    fearful: "&#128552;",
    weary: "&#128553;",
    sleepy: "&#128554;",
    tired: "&#128555;",
    grimacing: "&#128556;",
    cry: "&#128557;",
    amazed: "&#128558;",
    hushed: "&#128559;",
    scared: "&#128560;",
    terrified: "&#128561;",
    astonished: "&#128562;",
    flushed: "&#128563;",
    dizzy: "&#128565;",
    speechless: "&#128566;",
    mask: "&#128567;",
    puzzled: "&#128577;",
    smile: "&#128578;",
    unconvinced: "&#128580;",
    zip: "&#129296;",
    rich: "&#129297;",
    flu: "&#129298;",
    nerd: "&#129299;",
    thinking: "&#129300;",
    sick: "&#129301;",
    funny: "&#129313;",
    ill: "&#129314;",
    laughing: "&#129315;",
    dreaming: "&#129316;",
    lie: "&#129317;",
    sneeze: "&#129319;",
    wondering: "&#129320;",
    excited: "&#129321;",
    fool: "&#129322;",
    hush: "&#129323;",
    mad: "&#129324;",
    shy: "&#129325;",
    puke: "&#129326;",
    shocked: "&#129327;"
  };

// input_zone.addEventListener("input", () => {
//   for (const [key, value] of Object.entries(emojis_list)) {
//     if (input_zone.value.toLowerCase() == key.toLowerCase()) {
//       emoji.innerHTML = value;
//     }
//   }
// });


// good = document.getElementById("good")
// bed = document.getElementById("bed")

// function goodVale(){
//     var good = document.getElementById("good")
//     good.innerHTML ==`<span id="good">&#128515</span>`
// }

// goodVale()