<template>
  <div>
    <section id="clickaway" v-if="showModal">
      <div class="modal-mask">
        <div class="modal-wrapper">
          <div class="font center modal-container">
            <h1>{{ modalTitle }}</h1>
            <hr />
            <!-- Modal Body area -->
            <GChart
              :type="Table"
              :data="drillDownData"
              :options="chartOptionsDrillDown"
            />
            <!-- End Modal Body area -->
            <!-- Modal Footer area -->
            <div class="modal-footer">
              <slot name="footer">
                <button class="btn btn-success" @click="closeModal()">
                  Close
                </button>
              </slot>
            </div>
            <!-- End Modal Footer area -->
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// import AnalyzeGraphs from "@/components/Graphs/AnalyzeGraphs.vue";
import { mapGetters } from "vuex";

export default {
  name: "AnalyzeModal",
  // components: {
  //   AnalyzeGraphs,
  // },
  props: ["showModal", "modalTitle"],
  data() {
    return {
      Table: "Table",
      chartOptionsDrillDown: {
        alternatingRowStyle: true,
        height: 300,
        width: 800,
      }, // End Chart One Options
    };
  },
  computed: {
    ...mapGetters("analyze", ["drillDownData"]),
  }, // End Computed Area
  methods: {
    closeModal() {
      let modalClose = this.showModal;
      modalClose = false;
      this.$emit("close-modal", modalClose);
    },
    // Need to fix this duplication here
    onClickChild(value) {
      this.$emit("close-modal", value);
    },
  },
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}
.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
.modal-container {
  width: 800px;
  margin: 0px auto;
  padding: 20px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}
.modal-footer {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 20px;
}
</style>