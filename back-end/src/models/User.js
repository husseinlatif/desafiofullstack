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

    inclusionDate: {
        type: DataTypes.DATE,
        allowNull: false,
    },

    alterationDate: {
        type: DataTypes.DATE,
    },

    rules: {
        type: DataTypes.NUMBER,
        allowNull: false,
    },

    status: {
        type: DataTypes.STRING,
        allowNull: false,
    }

});

module.exports = User;