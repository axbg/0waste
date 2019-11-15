<template>
  <div id="app">
    <div class="container">
      <router-view/>
    </div>
  </div>
</template>

<style>
html, body, #app {
  height: 100%;
  background-color: whitesmoke;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
}
.container {
  width: 100%;
  height: 100%;
  background-color: whitesmoke;
}
a {
  text-decoration: none !important;
  color: black !important;
}
.sticky {
  position: sticky !important; 
  top:1px;
}
</style>