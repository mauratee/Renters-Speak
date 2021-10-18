"use strict";

// function initMap() {
//     const map = new google.maps.Map($('#map')[0], {
//       center: {
//         lat: 37.601773,
//         lng: -122.202870
//       },
//       zoom: 11,
//     });

// console.log(coordinates)

let basicMap;

function initMap() {
    const NYCoords = {
        // lat: coordinates[1],
        // lng: coordinates[0]
        lat: 40.70100109026094, 
        lng: -73.92472885964146
      };
      
    const basicMap = new google.maps.Map(
        document.querySelector('#map'),
        {
          center: NYCoords,
          zoom: 13,
        // Disables Default UI Controls
          disableDefaultUI: true,
          styles: [
            // from Google Developers Console, styled maps: Night Mode
            { elementType: "geometry", stylers: [{ color: "#242f3e" }] },
            { elementType: "labels.text.stroke", stylers: [{ color: "#242f3e" }] },
            { elementType: "labels.text.fill", stylers: [{ color: "#746855" }] },
            {
              featureType: "administrative.locality",
              elementType: "labels.text.fill",
              stylers: [{ color: "#d59563" }],
            },
            {
              featureType: "poi",
              elementType: "labels.text.fill",
              stylers: [{ color: "#d59563" }],
            },
            {
              featureType: "poi.park",
              elementType: "geometry",
              stylers: [{ color: "#263c3f" }],
            },
            {
              featureType: "poi.park",
              elementType: "labels.text.fill",
              stylers: [{ color: "#6b9a76" }],
            },
            {
              featureType: "road",
              elementType: "geometry",
              stylers: [{ color: "#38414e" }],
            },
            {
              featureType: "road",
              elementType: "geometry.stroke",
              stylers: [{ color: "#212a37" }],
            },
            {
              featureType: "road",
              elementType: "labels.text.fill",
              stylers: [{ color: "#9ca5b3" }],
            },
            {
              featureType: "road.highway",
              elementType: "geometry",
              stylers: [{ color: "#746855" }],
            },
            {
              featureType: "road.highway",
              elementType: "geometry.stroke",
              stylers: [{ color: "#1f2835" }],
            },
            {
              featureType: "road.highway",
              elementType: "labels.text.fill",
              stylers: [{ color: "#f3d19c" }],
            },
            {
              featureType: "transit",
              elementType: "geometry",
              stylers: [{ color: "#2f3948" }],
            },
            {
              featureType: "transit.station",
              elementType: "labels.text.fill",
              stylers: [{ color: "#d59563" }],
            },
            {
              featureType: "water",
              elementType: "geometry",
              stylers: [{ color: "#17263c" }],
            },
            {
              featureType: "water",
              elementType: "labels.text.fill",
              stylers: [{ color: "#515c6d" }],
            },
            {
              featureType: "water",
              elementType: "labels.text.stroke",
              stylers: [{ color: "#17263c" }],
            },
          ],
      
        }
      );

    console.log(basicMap)

    const sfMarker = new google.maps.Marker({
        position: NYCoords,
        title: 'New York City',
        icon: {url: "/static/img/map-marker.png",
                scaledSize: {
                    width: 55,
                    height: 55 
                }
                },
        map: basicMap
      });
};