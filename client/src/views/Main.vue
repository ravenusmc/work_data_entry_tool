<template>
  <div class='main-div'>
    <LocateAction />
    <ActionsForm v-if="actionFound" />
    <MissingAction v-if="actionNotFound" />
    <div class='btn-div' v-if="!showUserActions">
      <button
        @click.prevent="showAllUserActions"
        type="submit"
        name="login"
        class="btn btn-success"
      >
        Show User Action Table
      </button>
    </div>
    <div class='btn-div' v-if="showUserActions">
      <button
        @click.prevent="showAllUserActions"
        type="submit"
        name="login"
        class="btn btn-warning"
      >
        Hide User Action Table
      </button>
    </div>
    <Actions v-if="showUserActions" />
  </div>
</template>

<script>
import LocateAction from "@/components/main/LocateAction.vue";
import ActionsForm from "@/components/actionForms/ActionsForm.vue";
import MissingAction from "@/components/actionForms/MissingAction.vue";
import Actions from "@/components/main/Actions.vue";
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Main",
  data() {
    return {
      userTable: false,
    };
  },
  components: {
    LocateAction,
    ActionsForm,
    MissingAction,
    Actions,
  },
  computed: {
    ...mapGetters("data", ["actionFound", "actionNotFound", "showUserActions"]),
  },
  methods: {
    ...mapActions("data", ["showUserActionTable"]),
    showAllUserActions() {
      this.showUserActionTable();
    },
  },
};
</script>

<style scoped>

.main-div {
  min-height: 55vh;
}

.btn-div {
  margin: 1% 0 1% 0;
}

</style>

