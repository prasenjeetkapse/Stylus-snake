# Stylus-snake
***
Stylus Snake Game is the advanced version of old nokia snake game. In the old version we use to detect the direction of snake by "up", "down","left" and "right" key. But in the advance game we had obtain the direction of snake by the stylus or the object which will be capture by camera and by performing some operation it will decide the direction.

## STEPS FOLLOWED IN THE CODE

1. Librires used
     * opencv
     * numpy
     * pygame
     * random
2. Object of blue color is tracked using its HSV values.
3. To move snake left, right, top, bottom stylus should cross left, ridht, top, bottom boundaries respectibely.

![Screenshot 2021-10-11 162705](https://user-images.githubusercontent.com/83348619/136780389-631a1d5f-f0f5-4969-929d-e79eab178be4.png)

4. Created game environment using pygame.
   * Placed snake and food at random position on display bord.
   * score will display on window if you eat the food.
   * created 3 different hurdels,if you quite the game and start new game new hurdel will be displaye.
   * game will close 
      * if you hit hurdels.
     * if you touch head of snake to its body.
     * if you move snake out of the window.
   * If the game is close, press Q to quite the game or press C to continue.

  ![Screenshot 2021-10-11 165910](https://user-images.githubusercontent.com/83348619/136782886-8da48f56-c7bd-4227-ba0d-fa3c7eac353b.png)
  
  ## DEMO OF GAME
[click here to watch](https://drive.google.com/file/d/1r-gjU_bMJOuxgVawyNNWE9IMlnQeyaIH/view?usp=sharing)
  
  
