$(function() {
  showList();
  $("#cupcakes-form").on("submit", async function(e) {
    e.preventDefault();
    let flavor = $("#flavor").val()
    let size = $("#size").val()
    let rating = $("#rating").val()
    let image = $("#image").val()

    let response = await axios({
      method: 'post',
      url: '/api/cupcakes', 
      data: {
        flavor: flavor,
        size: size,
        rating: rating,
        image: image
      }
    });

    if (response.status === 201) showList();

  })
})

async function showList() {
  response = await axios({
    method: 'get',
    url: '/api/cupcakes'
  });
  let $cupcakeList = $("#cupcake-list");
  $cupcakeList.empty();
  for (let cupcake of response.data.cupcakes) {
    $cupcakeList.append(`<li>${cupcake.flavor}</li>`);
  }
}