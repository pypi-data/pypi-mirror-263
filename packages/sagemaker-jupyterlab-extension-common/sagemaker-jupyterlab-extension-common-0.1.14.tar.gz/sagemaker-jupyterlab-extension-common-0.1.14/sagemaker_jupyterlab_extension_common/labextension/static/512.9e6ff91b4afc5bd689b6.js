"use strict";(self.webpackChunk_amzn_sagemaker_jupyterlab_extension_common=self.webpackChunk_amzn_sagemaker_jupyterlab_extension_common||[]).push([[512,38],{512:(e,s,t)=>{t.r(s),t.d(s,{EventLog:()=>i,TelemetryHandler:()=>r});var n=t(901);class i{constructor(e){this._isDisposed=!1,this.handlers=e.handlers,this.allowedSchemas=e.allowedSchemas,this._eventSignal=new n.Signal(this),this._commandLog=[];for(const e of this.handlers)this._eventSignal.connect(e);e.commandRegistry?this.enableCommandEvents(e):console.log("No commandRegistry provided. Not publishing JupyterLab command events.")}get isDisposed(){return this._isDisposed}dispose(){this.isDisposed||(void 0!==this._saveInterval&&clearInterval(this._saveInterval),n.Signal.clearData(this),this._isDisposed=!0)}async recordEvent(e){this.isSchemaWhitelisted(e.schema)&&this.isSchemaValid(e)&&this._eventSignal.emit([Object.assign(Object.assign({},e),{publishTime:new Date})])}isSchemaValid(e){return!0}isSchemaWhitelisted(e){return this.allowedSchemas.indexOf(e)>-1}enableCommandEvents(e){var s;null===(s=e.commandRegistry)||void 0===s||s.commandExecuted.connect(((e,s)=>{const t=`org.jupyterlab.commands.${s.id}`;this.isSchemaWhitelisted(t)&&this._commandLog.push({schema:`org.jupyterlab.commands.${s.id}`,body:s.args,version:1,publishTime:new Date})})),this._saveInterval=setInterval((()=>{if(0===this._commandLog.length)return;const e=this._commandLog.splice(0);this._eventSignal.emit(e)}),void 0!==e.commandEmitIntervalSeconds?1e3*e.commandEmitIntervalSeconds:12e4)}}var a=t(920),o=t(840);class r{constructor(e={}){this.serverSettings=e.serverSettings||o.ServerConnection.makeSettings()}async save(e){const{serverSettings:s}=this,t=a.URLExt.join(s.baseUrl,"telemetry"),n={body:JSON.stringify(e),method:"PUT"};let i;try{i=await o.ServerConnection.makeRequest(t,n,s)}catch(e){throw new o.ServerConnection.NetworkError(e)}if(204!==i.status)throw new o.ServerConnection.ResponseError(i)}}}}]);