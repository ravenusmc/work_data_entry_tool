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
          id="Date_Created"
          type="text"
          v-model="Date_Created"
          :placeholder="dateCreatedData"
          onfocus="(this.type='date')"
        />
      </div>
      <div class="form-item">
        <label class="form-item__label" for="select">Recruit Action:</label>
        <div class="select-wrap">
          <select
            id="select"
            class="form-item__element form-item__element--select"
            required
            v-model="selectedValueRecruitAction"
          >
            <option disabled selected value="">
              Current Value: {{ changeRecruitAction }}
            </option>
            <option v-for="item in recruit_action" :key="item" :value="item">
              {{ item }}
            </option>
          </select>
        </div>
      </div>
      <!-- <div class="form-group">
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
          <option disabled>Please select one</option>
          <option v-for="item in Returned" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="Keyed">Action Keyed:</label>
        <select v-model="selectedValueKeyed">
          <option disabled>Please select one</option>
          <option v-for="item in Keyed" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div>
      <div class="form-group">
        <label for="firstname">Action Applied:</label>
        <select v-model="selectedValueApplied">
          <option disabled>Please select one</option>
          <option v-for="item in Applied" :key="item" :value="item">
            {{ item }}
          </option>
        </select>
      </div> -->
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
import moment from "moment";

export default {
  name: "DrillDownForm",
  computed: {
    ...mapGetters("data", ["actionData"]),
    actionNumberData() {
      return this.actionData[0];
    },
    dateCreatedData() {
      let convertedDate = new Date(this.actionData[1]);
      convertedDate.setDate(convertedDate.getDate() + 1);
      return moment(convertedDate).format("MM/DD/YYYY");
    },
    changeRecruitAction() {
      if (this.actionData[2]) return true;
      else return false;
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

      // NOA: "",
      // Authority: "",
      // Processor_ieNumber: "",
      // Date_Receieved: "",
      // Returned: [true, false],
      // selectedValueReturned: null,
      // Keyed: [true, false],
      // selectedValueKeyed: null,
      // Applied: [true, false],
      // selectedValueApplied: null,
    };
  },
  methods: {
    ...mapActions("data", ["updateData"]),
    updateAction() {
      console.log("HERE");
      const payload = {
        action_number: this.action_number,
        Date_Created: this.Date_Created,
        recruit_action: this.selectedValueRecruitAction,
        // action_id: this.actionID,
        // user_id: this.userObject["id"],

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