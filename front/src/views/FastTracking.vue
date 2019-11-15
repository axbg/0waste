<template>
  <div class="home-container">
    <md-toolbar class="md-dense md-accent sticky" md-elevation="1" >
      <h4>Hi {{this.username}}, ready to change the world?</h4>
      <div @click="logout" style="flex:2">
        <md-icon class="logout-icon">clear</md-icon>
      </div>
    </md-toolbar>
    <div class="feature-container">
      <md-card class="feature-control">
        <md-card-header>
          <div class="md-title">Fast Tracking</div>
        </md-card-header>
        <md-card-content class="card-content">
          <p>Upload one or more photos of different places and generate a heatmap of plastic waste</p>
          <div class="legend-container">
            <span style="color: red">Bottle |</span> 
            <span style="color: green"> Rope |</span> 
            <span style="color: orange"> Bag |</span> 
            <span style="color: blue"> Cap |</span>
            <span style="color: #FFFF00"> General Waste</span>
          </div>
          <div class="upload-container" v-if="displayUpload">
            <md-field>
              <label>Upload your photos</label>
              <md-file multiple @md-change="uploadPhotos"/>
            </md-field>
            <md-button class="md-raised md-accent loader" @click="processPhotos">Process photos</md-button>
          </div>
          <div v-else-if="loading">
            <md-progress-spinner class="md-accent" md-mode="indeterminate" :md-diameter="100"></md-progress-spinner>
            <h3>Looking for waste...</h3>
          </div>
          <div class="result-container" v-else="!displayUpload && !loading">
              <div v-for="photo in processedFiles">
                <div>
                  <h4>Detected {{photo.objects}} objects in the following image</h4>
                  <img v-bind:src="'data:image/jpg;base64,'+photo.annotated" class="fast-img"/>
                  <hr>
                </div>
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
    displayUpload: true,
    loading: false,
    files: [],
    processedFiles: []
  }),
  props: ["baseUrl"],
  methods: {
    logout: function() {
      localStorage.removeItem("username");
      location.reload();
    },
    uploadPhotos: function(files) {
      this.files = files;
      this.$toasted.show("Images were loaded")
    },
    processPhotos: async function() {
      if(this.files.length == 0) {
        this.$toasted.show("Images were not loaded");
        return;
      }
      
      this.loading = true;
      this.displayUpload = false;

      const formData = new FormData();

      for(let i = 0; i < this.files.length; i++) {
        formData.append("photos", this.files[i]);
      }
      
      const result = await this.$axios.post(this.baseUrl + "/fast", formData, {
        headers: {'Content-Type': 'multipart/form-data'}});

      for(let i = 0; i < result.data.annotated.length; i++) {
        this.processedFiles.push({annotated: result.data.annotated[i], objects: result.data.objects[i]});
      }
      this.loading = false;
    }
  },
  mounted: function() {
    this.username = localStorage.getItem("username");
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
.card-content *{
  text-align: center;
}
h4 {
  margin: 0;
}
.fast-img {
  max-height: 500px;
}
.legend-container {
  margin-bottom: 15px;
  text-align: center;
  font-size: 1.5em;
  text-shadow: 1px 1px black;
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