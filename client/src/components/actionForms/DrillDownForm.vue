<template>
  <div>
    <form class="contact-form">
      <div class="form-group">
        <label for="actionNumber">Action Number:</label>
        <input
          type="text"
          name="action_number"
          class="form-control"
          id="actionNumber"
          v-model="action_number"
          :placeholder="actionNumberData"
        />
      </div>
      <div class="form-group">
        <label for="Date_Created">Date Created:</label>
        <input
          type="date"
          name="ienumber"
          class="form-control"
          id="Date_Created"
          v-model="Date_Created"
          :placeholder="dateCreatedData"
        />
      </div>
      <div class="form-group">
        <label for="firstname">Recruit Action:</label>
        <select v-model="selectedValueRecruitAction">
          <option disabled value="">Please select one</option>
          <option v-for="item in recruit_action" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="NOA">Nature of Action:</label>
        <input
          type="text"
          name="NOA"
          class="form-control"
          id="NOA"
          v-model="NOA"
        />
      </div>
      <div class="form-group">
        <label for="Authority">Authority:</label>
        <input
          type="text"
          name="Authority"
          class="form-control"
          id="Authority"
          :placeholder="authorityData"
          v-model="Authority"
        />
      </div>
      <div class="form-group">
        <label for="Date_Receieved">Date Receieved:</label>
        <input
          type="date"
          name="ienumber"
          class="form-control"
          id="Date_Receieved"
          v-model="Date_Receieved"
        />
      </div>
      <div class="form-group">
        <label for="firstname">Action Returned:</label>
        <select v-model="selectedValueReturned">
          <option disabled value="">Please select one</option>
          <option v-for="item in Returned" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="Keyed">Action Keyed:</label>
        <select v-model="selectedValueKeyed">
          <option disabled value="">Please select one</option>
          <option v-for="item in Keyed" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="firstname">Action Applied:</label>
        <select v-model="selectedValueApplied">
          <option disabled value="">Please select one</option>
          <option v-for="item in Applied" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>

      <div class="btn-div">
        <button
          @click.prevent="updateAction"
          type="submit"
          name="login"
          class="btn btn-primary button-fix"
        >
          Submit
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "DrillDownForm",
  computed: {
    ...mapGetters("data", ["actionData"]),
    actionNumberData() {
      return this.actionData[0];
    },
    dateCreatedData() {
      return this.actionData[1]
    },
    authorityData() {
      return this.actionData[5];
    },
  },
  data() {
    return {
      action_number: "",
      Date_Created: "",
      recruit_action: [true, false],
      selectedValueRecruitAction: null,
      NOA: "",
      Authority: "",
      Processor_ieNumber: "", // Get from user
      Date_Receieved: "",
      Returned: [true, false],
      selectedValueReturned: null,
      Keyed: [true, false],
      selectedValueKeyed: null,
      Applied: [true, false],
      selectedValueApplied: null,
      test: "MIKE",
    };
  },
  methods: {
    ...mapActions("data", ["updateData"]),
    updateAction() {
      console.log("HERE")
      const payload = {
        action_number: this.action_number,
        Date_Created: this.Date_Created,
        // action_id: this.actionID,
        // user_id: this.userObject["id"],
        // recruit_action: this.selectedValueRecruitAction,

        // NOA: this.NOA,
        // Authority: this.Authority,
        // Processor_ieNumber: this.userObject["ieNumber"],
        // Date_Receieved: this.Date_Receieved,
        // Returned: this.selectedValueReturned,
        // Keyed: this.selectedValueKeyed,
        // Applied: this.selectedValueApplied,
      };
      console.log(payload);
      this.updateData({ payload });
    },
  },
};
//['TST-TST-2023-0001', 'Sun, 01 Jan 2023 00:00:00 GMT', 1, 1, 101, 'BWA', 'ie7046', 'Sun, 29 Jan 2023 00:00:00 GMT', 0, 1, __ob__: Observer]
// action_number, date_created, recruit_action, user_id, NOA,
//             Authority, Processor_ieNumber, Date_Receieved, Returned, Keyed
//             Applied
</script>

<style scoped>
.contact-form {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: 1fr 1fr;
  margin: 3% 20% 3% 20%;
}

.form-group {
  display: grid;
}

.button-fix {
  width: 100px;
  height: 50px;
}
</style>