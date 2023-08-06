// Get the file input and image container elements
const imageContainer = document.getElementById('imageContainer');
let imageCounter = 0;
var f = [];
// Listen for changes in the file input
document.getElementById('fileInput').addEventListener('change', handleFileSelect);

// Function to handle file selection
function handleFileSelect(event) {
  const files = event.target.files;
  // Loop through the selected files
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    
    // Check if the file is an image
    if (!file.type.startsWith('image/')) {
      continue;
    }
    
    
    // Create a FileReader to read the image data
    const reader = new FileReader();
    reader.onload = (function (file) {
      return function (e) {
        // When the image data is loaded, create an image item and add it to the container
        const imageItem = createImageItem(e.target.result, file);
        imageContainer.appendChild(imageItem);
        // updateFileInput();
      };
    })(file);
    // Read the image data as a Data URL
    reader.readAsDataURL(file);
  }
}

// Function to create an image item with the image and remove button
function createImageItem(dataUrl, file) {
  const imageItem = document.createElement('div');
  imageItem.classList.add('image-item');

  // Create an image element and set its source to the Data URL
  const image = document.createElement('img');
  image.src = dataUrl;
  imageItem.appendChild(image);

//   // Create a remove button and add a click event listener to remove the image item
//   const removeBtn = document.createElement('button');
//   removeBtn.classList.add('remove-btn');
//   removeBtn.textContent = 'X';
//   removeBtn.addEventListener('click', () => {
//     // Remove the image item from the container
//     imageContainer.removeChild(imageItem);
//     updateFileInput()
//   });
//   imageItem.appendChild(removeBtn);
  
  return imageItem;
}

