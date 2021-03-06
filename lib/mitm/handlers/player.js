const debug = require('debug')('mitm:player');
const _ = require('lodash');

module.exports = (mitmServer, app) => {
  mitmServer.addResponseHandler('GetPlayer', (_data) => {
    const data = _.cloneDeep(_data);
    const localPlayer = data.local_player || data.player_data;

    if (!localPlayer) {
      debug('local player undefined', _data);
      return data;
    }

    app.locals.player.updateWithProto(localPlayer);
    debug('PLAYER COMING THRU');
    return null;
  });
};
