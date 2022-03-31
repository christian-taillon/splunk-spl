<form theme="dark">
  <label>Splunk Template View</label>
  <description>I frequently find my self trying to remember what is required for a new view creation.</description>
  <fieldset autoRun="true" submitButton="true">
    <input type="time" token="time">
      <label>Time</label>
      <default>
        <earliest>-24h@h</earliest>
        <latest>now</latest>
      </default>
    </input>
  </fieldset>
</form>
