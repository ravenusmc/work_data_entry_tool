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
          <select id="select" required v-model="selectedValueRecruitAction">
            <option disabled selected :value="null">
              Current Value: {{ changeRecruitAction }}
            </option>
            <option v-for="item in recruit_action" :key="item" :value="item">
              {{ item }}
            </option>
          </select>
        </div>
      </div>
      <div class="form-group">
        <label for="NOA">Nature of Action:</label>
        <input
          type="text"
          name="NOA"
          class="form-control"
          id="NOA"
          v-model="NOA"
          :placeholder="noaData"
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
        <label for="ieNumber">IE Nuumber:</label>
        <input
          type="text"
          name="ieNumber"
          class="form-control"
          id="ieNumber"
          v-model="Processor_ieNumber"
          :placeholder="ieNumberData"
        />
      </div>
      <div class="form-group">
        <label for="Date_Receieved">Date Receieved:</label>
        <input
          id="Date_Receieved"
          type="text"
          v-model="Date_Receieved"
          :placeholder="dateReceivedData"
          onfocus="(this.type='date')"
        />
      </div>
      <div class="form-item">
        <label class="form-item__label" for="returned_select">Returned:</label>
        <div class="select-wrap">
          <select id="returned_select" required v-model="selectedValueReturned">
            <option disabled selected :value="null">
              Current Value: {{ returnedData }}
            </option>
            <option v-for="item in Returned" :key="item" :value="item">
              {{ item }}
            </option>
          </select>
        </div>
      </div>
      <div class="form-item">
        <label class="form-item__label" for="keyed_select">Returned:</label>
        <div class="select-wrap">
          <select id="keyed_select" required v-model="selectedValueKeyed">
            <option disabled selected :value="null">
              Current Value: {{ keyedData }}
            </option>
            <option v-for="item in Keyed" :key="item" :value="item">
              {{ item }}
            </option>
          </select>
        </div>
      </div>
      <div class="form-item">
        <label class="form-item__label" for="applied_select">Applied:</label>
        <div class="select-wrap">
          <select id="applied_select" required v-model="selectedValueApplied">
            <option disabled selected :value="null">
              Current Value: {{ appliedData }}
            </option>
            <option v-for="item in Applied" :key="item" :value="item">
              {{ item }}
            </option>
          </select>
        </div>
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
    noaData() {
      return this.actionData[4];
    },
    authorityData() {
      return this.actionData[5];
    },
    ieNumberData() {
      return this.actionData[6];
    },
    dateReceivedData() {
      let convertedDate = new Date(this.actionData[7]);
      convertedDate.setDate(convertedDate.getDate() + 1);
      return moment(convertedDate).format("MM/DD/YYYY");
    },
    returnedData() {
      if (this.actionData[8]) return true;
      else return false;
    },
    keyedData() {
      if (this.actionData[9]) return true;
      else return false;
    },
    appliedData() {
      if (this.actionData[10]) return true;
      else return false;
    },
  },
  data() {
    return {
      action_number: "",
      Date_Created: "",
      recruit_action: [true, false],
      selectedValueRecruitAction: null,
      NOA: "",
      ieNumber: "",
      Authority: "",
      Processor_ieNumber: "",
      Date_Receieved: "",
      Returned: [true, false],
      selectedValueReturned: null,
      Keyed: [true, false],
      selectedValueKeyed: null,
      Applied: [true, false],
      selectedValueApplied: null,
    };
  },
  methods: {
    ...mapActions("data", ["updateData"]),
    updateAction() {
      if (this.action_number === "") {
        this.action_number = this.actionData[0];
      }
      if (this.Date_Created === "") {
        this.Date_Created = this.actionData[1];
      }
      if (this.selectedValueRecruitAction === null) {
        this.selectedValueRecruitAction = this.actionData[2];
      }
      if (this.NOA === "") {
        this.NOA = this.actionData[4];
      }
      if (this.Authority === "") {
        this.Authority = this.actionData[5];
      }
      if (this.ieNumber === "") {
        this.ieNumber = this.actionData[6];
      }
      if (this.Date_Receieved === "") {
        this.Date_Receieved = this.actionData[7];
      }
      if (this.selectedValueReturned === null) {
        this.selectedValueReturned = this.actionData[8];
      }
      if (this.selectedValueKeyed === null) {
        this.selectedValueKeyed = this.actionData[9];
      }
      if (this.selectedValueApplied === null) {
        this.selectedValueApplied = this.actionData[10];
      }
      const payload = {
        action_number: this.action_number,
        Date_Created: this.Date_Created,
        recruit_action: this.selectedValueRecruitAction,
        NOA: this.NOA,
        Authority: this.Authority,
        ieNumber: this.ieNumber,
        Date_Receieved: this.Date_Receieved,
        Returned: this.selectedValueReturned,
        Keyed: this.selectedValueKeyed,
        Applied: this.selectedValueApplied,
        // action_id: this.actionID,
        // user_id: this.userObject["id"],
      };
      console.log(payload);
      this.updateData({ payload });
      let modalClose = this.showModal;
      modalClose = false;
      this.$emit("clicked", modalClose);
    },
  },
};
</script>

<style scoped>
.contact-form {
  display: grid;
  gap: 1.25rem;
  grid-template-columns: 1fr 1fr 1fr;
}

.form-group {
  display: grid;
}

.button-fix {
  width: 100px;
  height: 50px;
}
</style>