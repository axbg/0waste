<template>
  <div class="feature-container">
    <md-card class="feature-control">
      <md-card-header>
        <div class="md-title">Impact measurement</div>
      </md-card-header>
      <md-card-content class="card-content">
        <p>Upload one or more pairs of photos taken in the same place before and after collecting actions happened</p>
        <div class="legend-container">
          <span style="color: red">Bottle |</span>
          <span style="color: green">Rope |</span>
          <span style="color: orange">Bag |</span>
          <span style="color: blue">Cap |</span>
          <span style="color: #FFFF00">General Waste</span>
        </div>
        <div class="upload-container" v-if="displayUpload">
          <md-field>
            <label>Upload the "before" set of photos</label>
            <md-file multiple @md-change="uploadPhotosBefore" />
          </md-field>
        </div>
        <div class="upload-container" v-if="displayUpload">
          <md-field>
            <label>Upload the "after" set of photos</label>
            <md-file multiple @md-change="uploadPhotosAfter" />
          </md-field>
          <p>Notice: The photos should be selected in the same order</p>
          <md-button class="md-raised md-accent loader" @click="processPhotos">Process photos</md-button>
        </div>
        <div v-else-if="loading">
          <md-progress-spinner class="md-accent" md-mode="indeterminate" :md-diameter="100"></md-progress-spinner>
          <h3>Working hard. It may take a few seconds....</h3>
        </div>
        <div class="result-container" v-else>
          <div v-for="(photo, index) in processedFiles" :key="index">
            <md-card class="md-elevation-5">
              <div v-html="computeEvolution(photo.objectsBefore, photo.objectsAfter)"></div>
              <img v-bind:src="'data:image/jpg;base64,'+photo.before" class="impact-photo" />
              <span></span>
              <img v-bind:src="'data:image/jpg;base64,'+photo.after" class="impact-photo" />
              <br />
              <span>Before |</span>
              <span>After</span>
            </md-card>
          </div>
        </div>
      </md-card-content>
    </md-card>
  </div>
</template>

<script>
export default {
  name: "impact",
  data: () => ({
    displayUpload: true,
    loading: false,
    filesBefore: [],
    filesAfter: [],
    processedFiles: []
  }),
  props: ["baseUrl"],
  methods: {
    computeEvolution: function(before, after) {
      if (before > after) {
        return (
          '<h3 style="color: green">Congrats! The plastic waste level was reduced by ' +
          parseInt(((before - after) * 100) / before) +
          "%!😊<h3>"
        );
      } else if (before < after) {
        return (
          '<h3 style="color: red">Bad news! The plastic waste level was increased with ' +
          parseInt(((after - before) * 100) / after) +
          "%😢</h3>"
        );
      } else {
        return "<h3>Nothing has changed 😟</h3>";
      }
    },
    uploadPhotosBefore: function(files) {
      this.filesBefore = files;
      this.$toasted.show("Images were loaded");
    },
    uploadPhotosAfter: function(files) {
      this.filesAfter = files;
      this.$toasted.show("Images were loaded");
    },
    processPhotos: async function() {
      if (this.filesAfter.length !== this.filesBefore.length) {
        this.$toasted.show("The number of photos is not equal");
        return;
      }

      this.loading = true;
      this.displayUpload = false;

      const formData = new FormData();
      for (let i = 0; i < this.filesAfter.length; i++) {
        formData.append("before", this.filesBefore[i]);
        formData.append("after", this.filesAfter[i]);
      }

      const result = await this.$axios.post(
        this.baseUrl + "/impact",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" }
        }
      );

      for (let i = 0; i < result.data.beforeImages.length; i++) {
        this.processedFiles.push({
          before: result.data.beforeImages[i],
          after: result.data.afterImages[i],
          objectsBefore: result.data.beforeObjects[i],
          objectsAfter: result.data.afterObjects[i]
        });
      }
      this.loading = false;
    }
  }
};
</script>

<style>
.feature-container {
  margin: 0 auto;
  width: 100%;
}
.feature-control {
  margin: 0 auto;
  margin-top: 5vh;
  width: 80%;
}
.card-content * {
  text-align: center;
}
h4 {
  margin: 0;
}
.impact-photo {
  max-height: 350px;
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