<template>
  <div>
    <hr />
    <div>
      <h1>Welcome {{ userObject.first_name }}, here are your Actions:</h1>
      <form>
        <div class="form-group">
          <label for="actionNumber">Action Number:</label>
          <input
            type="text"
            name="action_number"
            id="actionNumber"
            size="20"
            v-model="action_number"
            placeholder="Enter Action Number"
          />
        </div>
        <div class="form-group">
          <label for="recruitAction">Recruit Action:</label>
          <select id="recruitAction" v-model="selectedValueRecruitAction">
            <option disabled value="">Please select one</option>
            <option v-for="item in recruit_action" :key="item" :value="item">
              {{ item }}
            </option>
          </select>
        </div>
        <div class="form-group">
          <label for="NOA">Nature of Action:</label>
          <input type="text" name="NOA" id="NOA" size="20" v-model="NOA" />
        </div>
        <div class="form-group">
          <label for="Authority">Authority:</label>
          <input
            type="text"
            name="Authority"
            id="Authority"
            size="20"
            v-model="Authority"
          />
        </div>
        <div class="btn-div">
          <button
            @click.prevent="filterTable"
            type="submit"
            name="login"
            class="btn btn-primary button-fix"
          >
            Submit
          </button>
        </div>
      </form>
      <GraphCard
        :typeOne="typeOne"
        :data="actionsByUser"
        :options="chartOptionsOne"
      />
    </div>
  </div>
</template>
	
<script>
import GraphCard from "@/components/Graphs/GraphCard.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Actions",
  components: {
    GraphCard,
  },
  data() {
    return {
      action_number: "",
      recruit_action: [true, false],
      selectedValueRecruitAction: null,
      NOA: "",
      Authority: "",
      division_name: "Bottoms",
      typeOne: "Table",
      chartOptionsOne: {
        title: "All Actions by User",
        legend: { position: "top" },
        colors: ["#f24867"],
        height: 500,
        allowHTML: true,
        animation: {
          duration: 1000,
          easing: "linear",
        },
        vAxis: {
          viewWindow: {
            min: 0,
          },
        },
      },
    };
  },
  computed: {
    ...mapGetters("session", ["userObject", "actionsByUser"]),
    ...mapGetters("data", ["actionsByUser"]),
  },
  methods: {
    ...mapActions("data", ["getSpecificActionsByUser"]),
    filterTable() {
      console.log("Hi");
      // const payload = {
      //   action_number: this.actionNumber,
      // };
      // this.submitMissingActionToDatabase({ payload });
    },
  },
  mounted() {
    const payload = {
      action_number: 7,
    };
    this.getSpecificActionsByUser({ payload });
  },
};
</script>

<style scoped>

form {
  display: flex;
  flex-direction: row;
  justify-content: center;
}

</style>