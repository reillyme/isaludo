# summer 2021
# basic setup for 52-card games
library(tidyverse)

suits = c('H','D','C','S')
values = c('A','2','3','4','5','6','7','8','9','10','J','Q','K')

create_deck = function(jokers = TRUE){
  deck = paste(values, suits)
  if(jokers){
    deck = c(deck, 'jo1','jo2')
  }
  return(deck)
}
