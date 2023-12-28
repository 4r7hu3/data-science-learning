### GOOGLE DATA ANALYTICS ###
library(tidyverse)
install.packages("palmerpenguins")
library(palmerpenguins)

# more readable
ggplot(penguins, aes(flipper_length_mm, body_mass_g)) +
  geom_point(na.rm = T)

# shortest
ggplot(data = penguins) + geom_point(mapping = aes(x = flipper_length_mm, y = body_mass_g))

# identify species by color
ggplot(penguins, aes(flipper_length_mm, body_mass_g, color = species)) +
  geom_point(na.rm = T)

# identify species by shape
ggplot(penguins, aes(flipper_length_mm, body_mass_g, shape = species)) +
  geom_point(na.rm = T)

# identify species by both color and shape
ggplot(penguins, aes(flipper_length_mm, body_mass_g, color = species, shape = species)) +
  geom_point(na.rm = T)

# fade effect
ggplot(penguins, aes(flipper_length_mm, body_mass_g, alpha = species)) +
  geom_point(na.rm = T)

# set color
ggplot(penguins, aes(flipper_length_mm, body_mass_g)) +
  geom_point(na.rm = T, colour = "purple")

# another representation
ggplot(penguins, aes(flipper_length_mm, body_mass_g)) +
  geom_smooth(na.rm = T)

# combined
ggplot(penguins, aes(flipper_length_mm, body_mass_g)) +
  geom_point(na.rm = T) +
  geom_smooth(na.rm = T)

# by species, with different lines
ggplot(penguins, aes(flipper_length_mm, body_mass_g, linetype = species)) +
  geom_smooth(na.rm = T)

# jitter (to see points clearer)
ggplot(penguins, aes(flipper_length_mm, body_mass_g)) +
  geom_jitter(na.rm = T)

# bar chart
ggplot(diamonds, aes(cut)) +
  geom_bar()

# stacked bar chart
ggplot(diamonds, aes(cut, fill = clarity)) +
  geom_bar()


# creating facets for ONE variable
ggplot(penguins, aes(flipper_length_mm, body_mass_g, color = species)) +
  geom_point(na.rm = T) +
  facet_wrap(~species)

# one more example
ggplot(diamonds, aes(cut)) +
  geom_bar() + 
  facet_wrap(~clarity)

# creating facets for TWO+ variables
ggplot(penguins, aes(flipper_length_mm, body_mass_g, color = species)) +
  geom_point(na.rm = T) + 
  facet_grid(sex~species)

# but it can be used for only one variable
ggplot(penguins, aes(flipper_length_mm, body_mass_g, color = species)) +
  geom_point(na.rm = T) +
  facet_grid(~sex)

# adding labels outside
ggplot(penguins, aes(flipper_length_mm, body_mass_g, color = species)) +
  geom_point(na.rm = T) +
  labs(title = "Palmer Penguins: Body Mass vs Flipper Length", subtitle = "Sample of 344 penguins", caption = "Data collect by Dr. Kristen Gorman")


# adding labels inside and outside
ggplot(penguins, aes(flipper_length_mm, body_mass_g, color = species)) +
  geom_point(na.rm = T) +
  labs(title = "Palmer Penguins: Body Mass vs Flipper Length", subtitle = "Sample of 344 penguins", caption = "Data collect by Dr. Kristen Gorman") +
  annotate("text", x = 220, y = 3500, label = "Gentoos are the largest", color = "darkblue", size = 5, angle = 45)
