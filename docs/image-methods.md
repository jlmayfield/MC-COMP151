# Key Image Module Methods

| Method Name | Example | Explanation |
| :-- | :-- | :-- |
| Image(filename) | img = image.Image(“cy.png”) | Create an Image object from the file cy.png. |
| EmptyImage() | img = image.EmptyImage(100,200) | Create an Image object that has all “White” pixels |
| getWidth() | w = img.getWidth() | Return the width of the image in pixels. |
| getHeight() | h = img.getHeight() | Return the height of the image in pixels. |
| getPixel(col,row) | p = img.getPixel(35,86) | Return the pixel at column 35, row 86. |
| setPixel(col,row,p) | img.setPixel(100,50,mp) | Set the pixel at column 100, row 50 to be mp. |
| Pixel(r,g,b) | Pixel(20,100,50) | Create a new pixel with 20 red, 100 green, and 50 blue. |
| getRed() | r = p.getRed() | Return the red component intensity. |
| getGreen() | r = p.getGreen() | Return the green component intensity. |
| getBlue() | r = p.getBlue() | Return the blue component intensity. |
| setRed() | p.setRed(100) | Set the red component intensity to 100. |
| setGreen() | p.setGreen(45) | Set the green component intensity to 45. |
| setBlue() | p.setBlue(156) | Set the blue component intensity to 156. |
