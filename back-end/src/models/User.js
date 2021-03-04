const DataTypes = require("sequelize");
const sequelize = require("../config/sequelize");

const User = sequelize.define('User', {

    username: {
        type: DataTypes.STRING,
        allowNull: false,
    },

    email: {
        type: DataTypes.STRING,
        allowNull: false,
    },
    
    rules: {
        type: DataTypes.SMALLINT,
        allowNull: false,
    },

    status: {
        type: DataTypes.STRING,
        allowNull: false,
    }

});

module.exports = User;