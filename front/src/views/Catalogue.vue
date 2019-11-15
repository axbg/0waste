<template>
  <div class="home-container">
    <md-toolbar class="md-dense md-accent sticky" md-elevation="1">
      <h4>Hi {{this.username}}, ready to change the world?</h4>
      <div @click="logout" style="flex:2">
        <md-icon class="logout-icon">clear</md-icon>
      </div>
    </md-toolbar>
    <div class="feature-container">
      <md-card class="feature-control">
        <md-card-header>
          <div class="md-title">Catalogue</div>
        </md-card-header>
        <md-card-content class="catalogue-card-content">
          <p>Where all your processed images live</p>
          <div v-if="loading">
            <md-progress-spinner class="md-accent" md-mode="indeterminate" :md-diameter="100"></md-progress-spinner>
            <h3>Loading everything...</h3>
          </div>
          <div v-else>
            <div v-for="photo in processedFiles" class="image-gallery">
              <img v-bind:src="'data:image/jpg;base64,'+photo" class="image-entry"/>
            </div>
          </div>
        </md-card-content>
      </md-card>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  data: () => ({
    username: "",
    loading: true,
    processedFiles: []
  }),
  props: ["baseUrl"],
  methods: {
    logout: function() {
      localStorage.removeItem("username");
      location.reload();
    },
    loadPhotos: async function() {
        const result = await this.$axios.get(this.baseUrl + "/catalogue");
        this.processedFiles = result.data.photos;
        this.loading = false;
    }
  },
  mounted: function() {
    this.username = localStorage.getItem("username");
    this.loadPhotos();
  }
};
</script>

<style>
.home-container {
  display: inline-block;
  width: 100%;
}
.logout-icon {
  float: right;
  cursor: pointer;
}
.username-container {
  float: left;
  margin-left: 2%;
}
.feature-container {
  margin: 0 auto;
  width: 100%;
}
.feature-control {
  margin: 0 auto;
  margin-top: 5vh;
  width: 80%;
}
.catalogue-card-content {
  text-align: center;
}
h4 {
  margin: 0;
}
.image-gallery {
  display:inline-block;
}
.image-gallery img {
  max-height: 300px;
}
.image-entry {
  margin: 2px;
}
@media only screen and (max-width: 1400px) {
  .feature-control {
    width: 90%;
  }
}
@media only screen and (max-width: 700px) {
  .feature-control {
    width: 90%;
  }
}
</style>