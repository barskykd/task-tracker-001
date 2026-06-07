var Api = (() => {
  var __defProp = Object.defineProperty;
  var __getOwnPropDesc = Object.getOwnPropertyDescriptor;
  var __getOwnPropNames = Object.getOwnPropertyNames;
  var __hasOwnProp = Object.prototype.hasOwnProperty;
  var __export = (target, all) => {
    for (var name in all)
      __defProp(target, name, { get: all[name], enumerable: true });
  };
  var __copyProps = (to, from, except, desc) => {
    if (from && typeof from === "object" || typeof from === "function") {
      for (let key of __getOwnPropNames(from))
        if (!__hasOwnProp.call(to, key) && key !== except)
          __defProp(to, key, { get: () => from[key], enumerable: !(desc = __getOwnPropDesc(from, key)) || desc.enumerable });
    }
    return to;
  };
  var __toCommonJS = (mod) => __copyProps(__defProp({}, "__esModule", { value: true }), mod);

  // app/static/js/taskTackerAppAPI.ts
  var taskTackerAppAPI_exports = {};
  __export(taskTackerAppAPI_exports, {
    StatusEnum: () => StatusEnum,
    commentariesCreate: () => commentariesCreate,
    commentariesList: () => commentariesList,
    commentariesRetrieve: () => commentariesRetrieve,
    getCommentariesCreateUrl: () => getCommentariesCreateUrl,
    getCommentariesListUrl: () => getCommentariesListUrl,
    getCommentariesRetrieveUrl: () => getCommentariesRetrieveUrl,
    getTasksCreateUrl: () => getTasksCreateUrl,
    getTasksDestroyUrl: () => getTasksDestroyUrl,
    getTasksListUrl: () => getTasksListUrl,
    getTasksPartialUpdateUrl: () => getTasksPartialUpdateUrl,
    getTasksRetrieveUrl: () => getTasksRetrieveUrl,
    getTasksUpdateUrl: () => getTasksUpdateUrl,
    getUsersListUrl: () => getUsersListUrl,
    getUsersRetrieveUrl: () => getUsersRetrieveUrl,
    tasksCreate: () => tasksCreate,
    tasksDestroy: () => tasksDestroy,
    tasksList: () => tasksList,
    tasksPartialUpdate: () => tasksPartialUpdate,
    tasksRetrieve: () => tasksRetrieve,
    tasksUpdate: () => tasksUpdate,
    usersList: () => usersList,
    usersRetrieve: () => usersRetrieve
  });
  var StatusEnum = {
    NUMBER_0: 0,
    NUMBER_1: 1
  };
  var getCommentariesListUrl = (params) => {
    const normalizedParams = new URLSearchParams();
    Object.entries(params || {}).forEach(([key, value]) => {
      if (value !== void 0) {
        normalizedParams.append(key, value === null ? "null" : String(value));
      }
    });
    const stringifiedParams = normalizedParams.toString();
    return stringifiedParams.length > 0 ? `/commentaries/?${stringifiedParams}` : `/commentaries/`;
  };
  var commentariesList = async (params, options) => {
    const res = await fetch(
      getCommentariesListUrl(params),
      {
        ...options,
        method: "GET"
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getCommentariesCreateUrl = () => {
    return `/commentaries/`;
  };
  var commentariesCreate = async (commentaryWrite, options) => {
    const res = await fetch(
      getCommentariesCreateUrl(),
      {
        ...options,
        method: "POST",
        headers: { "Content-Type": "application/json", ...options?.headers },
        body: JSON.stringify(commentaryWrite)
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getCommentariesRetrieveUrl = (id) => {
    return `/commentaries/${id}/`;
  };
  var commentariesRetrieve = async (id, options) => {
    const res = await fetch(
      getCommentariesRetrieveUrl(id),
      {
        ...options,
        method: "GET"
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getTasksListUrl = () => {
    return `/tasks/`;
  };
  var tasksList = async (options) => {
    const res = await fetch(
      getTasksListUrl(),
      {
        ...options,
        method: "GET"
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getTasksCreateUrl = () => {
    return `/tasks/`;
  };
  var tasksCreate = async (TaskWriteSerializer, options) => {
    const res = await fetch(
      getTasksCreateUrl(),
      {
        ...options,
        method: "POST",
        headers: { "Content-Type": "application/json", ...options?.headers },
        body: JSON.stringify(TaskWriteSerializer)
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getTasksRetrieveUrl = (id) => {
    return `/tasks/${id}/`;
  };
  var tasksRetrieve = async (id, options) => {
    const res = await fetch(
      getTasksRetrieveUrl(id),
      {
        ...options,
        method: "GET"
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getTasksUpdateUrl = (id) => {
    return `/tasks/${id}/`;
  };
  var tasksUpdate = async (id, TaskWriteSerializer, options) => {
    const res = await fetch(
      getTasksUpdateUrl(id),
      {
        ...options,
        method: "PUT",
        headers: { "Content-Type": "application/json", ...options?.headers },
        body: JSON.stringify(TaskWriteSerializer)
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getTasksPartialUpdateUrl = (id) => {
    return `/tasks/${id}/`;
  };
  var tasksPartialUpdate = async (id, patchedTaskWriteSerializer, options) => {
    const res = await fetch(
      getTasksPartialUpdateUrl(id),
      {
        ...options,
        method: "PATCH",
        headers: { "Content-Type": "application/json", ...options?.headers },
        body: JSON.stringify(patchedTaskWriteSerializer)
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getTasksDestroyUrl = (id) => {
    return `/tasks/${id}/`;
  };
  var tasksDestroy = async (id, options) => {
    const res = await fetch(
      getTasksDestroyUrl(id),
      {
        ...options,
        method: "DELETE"
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : void 0;
    return { data, status: res.status, headers: res.headers };
  };
  var getUsersListUrl = () => {
    return `/users/`;
  };
  var usersList = async (options) => {
    const res = await fetch(
      getUsersListUrl(),
      {
        ...options,
        method: "GET"
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  var getUsersRetrieveUrl = (id) => {
    return `/users/${id}/`;
  };
  var usersRetrieve = async (id, options) => {
    const res = await fetch(
      getUsersRetrieveUrl(id),
      {
        ...options,
        method: "GET"
      }
    );
    const body = [204, 205, 304].includes(res.status) ? null : await res.text();
    const data = body ? JSON.parse(body) : {};
    return { data, status: res.status, headers: res.headers };
  };
  return __toCommonJS(taskTackerAppAPI_exports);
})();
