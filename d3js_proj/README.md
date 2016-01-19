# eventbrite

This is a simple javascript application that uses D3.js and eventbrite API to generate a choropleth. The application requests
eventbrite for performance related events happening within a week. Each request returns a maximum of 50 results. After every 
request, the choropleth is updated. A progress bar on top represents the proportion of results received.

The choropleth has been made interactive by adding mouseover events that include highlighting and labels.

Project live at [iahmed.me/eventbrite](http://iahmed.me/eventbrite).
