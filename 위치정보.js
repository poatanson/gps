navigator.geolocation.getCurrentPosition(position => {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    console.log(`위도: ${latitude}, 경도: ${longitude}`);
});