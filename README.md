# Depthify

Depthify is a Blender addon that creates a 3D surface from a depth map image using adaptive subdivision and displacement. It also allows for a separate image to be applied for the diffusion or color of the material.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Hints and Tips](#hints-and-tips)
- [Other Use Cases](#other-use-cases)
- [Acknowledgements and Credits](#acknowledgements-and-credits)
- [License](#license)

## Overview

Depth maps are images that encode the distance or depth of each pixel from the camera. They are often used in computer vision, 3D scanning, photogrammetry, and other applications that require reconstructing 3D geometry from 2D images. However, creating a 3D surface from a depth map image can be challenging and time-consuming, especially for beginners or non-experts.

Depthify is a Blender addon that simplifies this process and allows anyone to create a 3D surface from a depth map image with just a few clicks. It uses adaptive subdivision and displacement to add detail to the shape of the surface without requiring a high-poly mesh. It also allows for a separate image to be applied for the diffusion or color of the material, creating realistic and stunning results.

Depthify can be used for various purposes, such as:

- Creating 3D models from photos or scans
- Enhancing or modifying existing 3D models
- Generating terrain or landscapes
- Creating artistic or abstract effects
- And more!

[Back to top](#table-of-contents)

## Features

Depthify has the following features:

- Import any depth map image file (PNG or JPEG) as a plane using the Import Images as Planes addon that Blender comes with
- Set up adaptive subdivision and displacement for the plane using Cycles render engine
- Invert the depth map if needed
- Adjust the depth scale to control the amount of displacement
- Set up a background plane with a solid color
- Join the depth plane and the background plane into one object
- Render the 3D surface to an image file with various options such as anti-aliasing, output format, and output name
- Save the rendered image file to any output folder

[Back to top](#table-of-contents)

## Installation

To install Depthify, follow these steps:

1. Download the `depthify.zip` file from the [releases](https://github.com/microsoft-bing-search-assistant/depthify/releases) page.
2. Open Blender and go to Edit > Preferences > Add-ons.
3. Click on Install and browse to the `depthify.zip` file.
4. Enable the Depthify addon by checking the box next to it.

[Back to top](#table-of-contents)

## Usage

To use Depthify, follow these steps:

1. Select an object in the 3D viewport.
2. Go to Object Properties > Depthify panel.
3. Click on the folder icon next to Image File and select a depth map image file (PNG or JPEG).
4. Click on the folder icon next to Output File and select an output folder where the rendered image will be saved.
5. Optionally, adjust the other options such as Invert Depth, Depth Scale, Background Color, Anti-Aliasing, Output Format and Output Name.
6. Click on the Depthify button to create a 3D surface from the depth map image and render it to an image file.

[Back to top](#table-of-contents)

## Hints and Tips

Here are some hints and tips for using Depthify:

- The quality and resolution of the depth map image will affect the quality and resolution of the 3D surface. Try to use high-quality and high-resolution depth maps for best results.
- The depth scale option can be used to control how much displacement is applied to the surface. A higher value will create more depth and relief, while a lower value will create less depth and relief. Experiment with different values to find the best one for your image.
- The invert depth option can be used to invert the depth map if it is inverted by default. Some depth maps encode closer pixels as darker values and farther pixels as lighter values, while others do the opposite. If your depth map looks wrong or inverted, try toggling this option on or off.
- The background color option can be used to change the color of the background plane that is created behind the depth plane. This can be useful to create contrast or harmony with the depth plane, or to match the color of the original image if it has a solid background.
- The anti-aliasing option can be used to enable or disable anti-aliasing for the rendered image. Anti-aliasing is a technique that smooths out jagged edges and improves the quality of the image. However, it can also increase the render time and memory usage. If you want a faster render or a smaller file size, you can disable this option.
- The output format option can be used to choose the format of the rendered image file. You can choose from PNG, JPEG, BMP, or TIFF formats. PNG and TIFF are lossless formats that preserve all the details and quality of the image, but they also have larger file sizes. JPEG and BMP are lossy formats that compress the image and reduce the file size, but they also lose some details and quality. Choose the format that suits your needs and preferences.
- The output name option can be used to change the name of the rendered image file. By default, it is set to "output", but you can change it to anything you want. Make sure to include the file extension that matches the output format you chose.

[Back to top](#table-of-contents)

## Other Use Cases

Depthify can be used for various purposes, such as:

- Creating 3D models from photos or scans: You can use Depthify to create 3D models from photos or scans that have depth information, such as stereo images, depth cameras, lidar scanners, etc. You can also use online tools or software to generate depth maps from single images, such as [Depth Map Creator](https://depth-map.net/), [3D Photo Creator](https://3d-photo-creator.com/), [Depthy](https://depthy.me/), etc.
- Enhancing or modifying existing 3D models: You can use Depthify to enhance or modify existing 3D models by applying depth maps to them. For example, you can add more detail or texture to a model by using a depth map of a similar object or material, such as wood, stone, metal, etc. You can also use Depthify to create variations or mutations of a model by using a depth map of a different object or material, such as animal skin, scales, fur, etc.
- Generating terrain or landscapes: You can use Depthify to generate terrain or landscapes by using depth maps of real or fictional places, such as mountains, valleys, islands, planets, etc. You can also use Depthify to create custom terrain or landscapes by using depth maps of abstract shapes or patterns, such as fractals, noise, waves, etc.
- Creating artistic or abstract effects: You can use Depthify to create artistic or abstract effects by using depth maps of anything you want, such as paintings, drawings, logos, symbols, text, etc. You can also use Depthify to create surreal or psychedelic effects by using depth maps of distorted or inverted images, such as optical illusions, kaleidoscopes, mirrors, etc.

[Back to top](#table-of-contents)

## Acknowledgements and Credits

Depthify is based on the following resources and references:

- [Blender Manual - Displacement](https://docs.blender.org/manual/en/latest/render/materials/components/displacement.html)
- [Blender adaptive subdivision for better displacement - YouTube](https://www.youtube.com/watch?v=A5PBvDCSJxs)
- [Change Displacement Scale and have Adaptive Subdivision enabled - Blender Developer](https://developer.blender.org/T82958)
- [PEP 8 - Style Guide for Python Code](https://pep8.org/)
- [Python Developer Best Practices for 2022 - Developer.com](https://www.developer.com/languages/python-best-practices/)
- [How To Write A Readme File For Github - Code With Harry](https://www.codewithharry.com/blogpost/how-to-write-a-readme-file-for-github)

[Back to top](#table-of-contents)

## License

Depthify is licensed under the MIT License. See [LICENSE](https://github.com/microsoft-bing-search-assistant/depthify/blob/main/LICENSE) for more information.

[Back to top](#table-of-contents)
