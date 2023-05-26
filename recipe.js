const input = document.getElementById("input");
const submit = document.getElementById("submit");
const output = document.getElementById("output");

submit.addEventListener("click", function () {
  const inputValue = input.value;
  if (inputValue === "What ingredients do I need to make chicken and rice?") {
    output.innerHTML = "You will need chicken, rice, and spices like salt, pepper, and garlic powder.";
  } else if (inputValue === "How do I make stir-fried vegetables?") {
    output.innerHTML = "To make stir-fried vegetables, you will need vegetables like broccoli, carrots, and peppers and spices like salt, pepper, and garlic powder. To cook, heat a large pan over medium heat, add the spices and vegetables, and stir-fry until they are cooked to your liking.";
  } else {
    output.innerHTML = "I am sorry, I do not have a recipe for that.";
  }
});
